import logging

# Instantiate a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('root')

# Constant
SITE_PERM_ORDER = ['user', 
                   'developer', 
                   'site_admin']

GROUP_PERM_ORDER = ['ro', 
                    'rw', 
                    'admin']

PROJECT_MIN_PERM = ['containers_view_metadata', 
                    'analyses_view_metadata',
                    'files_view_metadata',
                    'files_view_contents',
                    'files_download',
                    'tags_view',
                    'notes_view',
                    'project_permissions_view',
                    'gear_rules_view',
                    'data_views_view',
                    'session_templates_view',
                    'jobs_view']


# Functions
def check_user_permission(fw_client, min_reqs, group=None, project=None, show_compatible=True):
    """Check if user has the right permission to proceed.
    
    Args:
        fw_client (flywheel.client): A Flywheel API Client.
        min_reqs (dict): Minimum requirements.
        group (str): Group label. Default to None.
        project (str): Project label. Default to None.
        show_compatible (bool): Print out more information about compatible user permission. Default to True.
        
    Returns:
        bool: Returns True if user has the right permission, False otherwise 
    
    """

    has_perm = has_min_permissions(fw_client, min_reqs, group, project)
    
    # Print out compatible group and project if user's selections do not meet the requirements
    if show_compatible and not has_perm:
        list_compatible(fw_client, min_reqs)
        
    return has_perm

def has_min_permissions(fw_client, min_reqs, group=None, project=None):
    """Check whether user meets the minimum permission
    
    Args:
        fw_client(flywheel.client): A Flywheel API Client
        min_reqs (dict): Minimum requirements.
        group (str): Group label. Default to None.
        project (str): Project label. Default to None.
        
    Returns:
    bool: Returns True if user meets the minimum permission, False otherwise
    """
    user = fw_client.get_current_user()
    
    
    if not has_site_perm(user, min_reqs):
        return False
    if group and not has_group_perm(fw_client, user,group, min_reqs['group']):
        return False
    if project and not has_project_perm(fw_client, user, project, min_reqs['project']):
        return False
    
    # Returns true if site, group and/or project permissions are met
    return True

    

    
def has_site_perm(user, min_reqs):
    """Check if user has the right permission on the site container
    
    Args:
        user (flywheel.user): Flywheel User modules
        min_reqs (dict): Minimum requirements
    
    Returns:
        bool: Returns True if user meets the minimum site permission, False otherwise
    
    """
    
    if SITE_PERM_ORDER.index(user['roles'][0]) >= SITE_PERM_ORDER.index(min_reqs['site']):
        return True
    else:
        return False
    
    
def has_group_perm(fw_client, user, group, group_perm):
    """Check if user has the right permission on the group container
    
    Args:
        fw_client(flywheel.client): A Flywheel API Client
        user (flywheel.user): Flywheel User modules
        group (str): Group label
        group_perm (list): Minimum group permission
    
    Returns:
        bool: Returns True if user meets the minimum group permission, False otherwise
    
    """
    
    group_container = fw_client.lookup(group)
    group_permission = fw_client.get_group_user_permission(group_container.id, user['_id'])
    
    if GROUP_PERM_ORDER.index(group_permission['access']) >= GROUP_PERM_ORDER.index(group_perm):
        return True
    else:
        return False
    
    
def has_project_perm(fw_client, user, project, min_proj_reqs):
    """Check if user has the right permission on the project container
    
    Args:
        fw_client(flywheel.client): A Flywheel API Client
        user (flywheel.user): Flywheel User modules
        project (str): Project label
        min_proj_reqs (dict): Minimum project requirements/actions
    
    Returns:
        bool: Returns True if user meets the minimum project permission, False otherwise
    
    """
    
    project_container = fw_client.projects.find_first(f'label={project}')
    if not project_container:
        raise ValueError(f'No project found labelled: {project}')    
    user_perms = fw_client.get_project_user_permission(project_container.id, user['_id'])
    
    # Combine all required actions 
    proj_reqs = list(set(min_proj_reqs) | set(PROJECT_MIN_PERM))
    
    user_actions = list()
    
    for role_id in user_perms['role_ids']:
        role = fw_client.get_role(role_id)
        if user_actions:
            user_actions = list(set(user_actions) | set(role['actions']))
        else:
            user_actions = role['actions']
            
    if all(action in user_actions for action in proj_reqs):
        return True
    else:
        return False
    
    
    
    

def list_compatible(fw_client, min_reqs):
    """Provide a list of compatible container that meets the minimum requirements
    
    Args:
        fw_client(flywheel.client): A Flywheel API Client
        min_reqs (dict): Minimum requirements

    
    """
    user = fw_client.get_current_user()
    

    compatible_group = list()
    compatible_project = list()

    for container, perms in min_reqs.items():
        if container == 'site':
            
            if not has_site_perm(user, min_reqs):
                log.warning(
                    f'Please contact your site admin to get at least {perms} permission on your Flywheel Instance')
            else:
                log.info('You have the right site permission.')
            
            
        elif container == 'group':
            for group in fw_client.groups():
                if has_group_perm(fw_client, user, group.id, perms):
                    compatible_group.append(group.id)
                
                    
        elif container == 'project':
            proj_reqs = list(set(perms) | set(PROJECT_MIN_PERM))
            for project in fw_client.projects():
                if has_project_perm(fw_client, user, project.label, proj_reqs):
                    compatible_project.append(project.label)
                
                
    if compatible_group:
        group_list = ', '.join(map(str, compatible_group))
        log.info(f'You have the minimum required permission on the following group(s) {group_list}')
    if compatible_project:
        project_list = ', '.join(map(str, compatible_project))
        log.info(f'You have the minimum required permission on the following project(s) {project_list}')
