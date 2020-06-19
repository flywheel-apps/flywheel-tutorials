
def check_user_permission(fw_client, min_reqs, group=None, project=None, show_info=True):


    has_perm = is_user_meet_min_perm(fw_client, min_reqs, group, project)

    if show_info and not has_perm:
        list_compatible(fw_client, min_reqs)
    return has_perm


def is_user_meet_min_perm(fw_client, min_reqs, group=None, project=None):
    user = fw_client.get_current_user()
    proj_reqs = list(set(min_reqs['project']) | set(PROJECT_MIN_PERM))

    if SITE_PERM_ORDER.index(user['roles'][0]) >= SITE_PERM_ORDER.index(min_reqs['site']):
        if group:
            # group container
            group_container = fw_client.lookup(group)
            group_permission = fw_client.get_group_user_permission(group_container.id, user['_id'])
            if GROUP_PERM_ORDER.index(group_permission['access']) >= GROUP_PERM_ORDER.index(min_reqs['group']):
                if project:
                    # Project container
                    proj_reps = list(set(PROJECT_MIN_PERM) | set(min_reqs['project']))
                    project_container = group_container.projects.find_first(f'label={project}')
                    project_permission = fw_client.get_project_user_permission(project_container.id, user['_id'])
                    role_perm = fw_client.get_role(project_permission['role_ids'][0])
                    if set(role_perm['actions']).symmetric_difference(set(proj_reps)):
                        # When there is a difference between what is needed
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return False
        else:
            return True
    else:
        return False


def list_compatible(fw_client, min_reqs):
    user = fw_client.get_current_user()
    compatible_group = list()
    compatible_project = list()

    for container in min_reqs:
        if container == 'site':
            if SITE_PERM_ORDER.index(user['roles'][0]) >= SITE_PERM_ORDER.index(min_reqs['site']):
                log.info('You have the right site permission.')
            else:
                site_reqs = min_reqs['site']
                log.warning(
                    f'Please contact your site admin to get at least {site_reqs} permission on your Flywheel Instance')
        elif container == 'group':
            for group in fw_client.groups():
                group_permission = fw_client.get_group_user_permission(group.id, user['_id'])
                if GROUP_PERM_ORDER.index(group_permission['access']) >= GROUP_PERM_ORDER.index(min_reqs['group']):
                    compatible_group.append(group.label)
        elif container == 'project':
            for project in fw_client.projects():
                proj_reps = list(set(PROJECT_MIN_PERM) | set(min_reqs['project']))
                project_permission = fw_client.get_project_user_permission(project.id, user['_id'])
                role_perm = fw_client.get_role(project_permission['role_ids'][0])
                if not set(role_perm['actions']).symmetric_difference(set(proj_reps)):
                    compatible_project.append(project.label)
    if compatible_group:
        group_list = ', '.join(map(str, compatible_group))
        log.info(f'You have the minimum required permission on the following group(s) {group_list}')
    if compatible_project:
        project_list = ', '.join(map(str, compatible_project))
        log.info(f'You have the minimum required permission on the following project(s) {project_list}')
