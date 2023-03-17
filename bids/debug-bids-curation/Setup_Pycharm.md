# Debug BIDS Curation

## Set up Debugger

In PyCharm, open this directory as a project.  Set the interpreter for this project by going to 
Preferences (command-comma), open "Project" and select "Project Interpreter".  Then click on the
little gear and select "Add".

![Set the project interpreter](pics/Set_project_interpreter.png)

Choose "Pipenv" for the environment:

![Select Pipenv](pics/Select_Pipenv.png)

The environment will be empty at first.  Click the "+" to add a package, search for "flywheel"
and select "flywheel-bids".

![Install flywheel-bids](pics/Install_flywheel-bids.png)

Click on the "Add Configuration..." button near the top right of the PyCharm window. 

![Select Add Configuration](pics/Select_Add_Configuration.png)

Click on the "+" and select "Python" to add a Python configuration.

![Add A Python Configuration](pics/Add_A_Python_Configuration.png)

Give it a name, then set the script path:

![Give it a name](pics/Give_it_a_name.png)

Select "runCurate.py"

![Select runCurate.py](pics/Select_runCurate.py.png)

Type in parameters to pass in to [flywheel_bids/curate_bids.py](https://gitlab.com/flywheel-io/public/bids-client/-/blob/0.9.0/flywheel_bids/curate_bids.py#L252)

For example:

`--api-key ss.ce.flywheel.io:YadaYadaYadaYadaHo -p atbs-study --session-only --session 5a19c137d8e083001c0b340e --reset`

![Type in Parameters](pics/Type_in_Parameters.png)

Open "runCurate.py" and set a breakpoint at "main()"

![Open runCurate](pics/Open_runCurate.py.png)

Then launch the debugger:

![Launch the debugger](pics/Launch_the_debugger.png)

Click on the "Console" tab, and you'll see you are running, yay!

![Click on the Console.png](pics/Click_on_the_Console.png)

Click on the "Debugger" tab and step in by clicking on the blue down-arrow:

![Click on Debugger](pics/Click_on_Debugger.png)

You will find yourself at the first executable line of `curate_bids.py`.  From
there, set other breakpoints and, well, you know the drill.  Squish that bug.

You can find other source files under "External Libraries"

![Find other source files](pics/Find_other_source_files.png)
