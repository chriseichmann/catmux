# Catmux

## About
Catmux is a little helper to run a tmux session with multiple windows and panes with just one
command. It is inspired and functionally very similar to
[tmuxinator](https://github.com/tmuxinator/tmuxinator), but without the project management feature
which is in my opinion kind of an overhead.

Session configs can be stored anywhere and have to be given as an argument.

## DISCLAIMER - Early package
This package is currently in development phase. It's interface might completely change and/or
functionality might be moved around or even removed without notice. Use it at your own risks and
report issues and problems :)

However, by now it has been used productively in four different projects by different people without
problems, so I would consider it 'working'.

If you try out catmux and you find anything you're missing, anything that doesn't work as expected,
or is clearly a bug, please create an issue here, I'll be happy to answer to them. Of course, merge
requests are always welcome, as well :)

## Motivation
In most of our ROS projects at work we use shell output for almost all nodes to get log information
during runtime. Having all this in one window where you start your "Start it all"-launchfile makes
it very hard to follow the log of a specific node. Starting everything in separate windows is quite
a lot of work and requires documentation overhead in sense of documenting which launchfiles or nodes
have to be started.

At a conference I caught the idea to use tmux scripting to orchestrate all this in one tmux session.
However, quickly I noticed that creating these scripts is a daunting task as you'll have to type in
a lot of commands over and over again and as soon as you wanted to do things a little different such
as not starting a particular launchfile if a certain parameter was set, things got complicated.

I liked the yaml-syntax of [tmuxinator](https://github.com/tmuxinator/tmuxinator), but that tool
didn't quite hit the spot. I wanted to have something that can be easily integrated into a ROS
project and I definitely wanted something that saves the config per project and not all configs at
one central spot on a particular machine.

## Installation
Catmux is a pure python package and as such it is installable via pip.
After cloning this repository call `pip3 install --user .` in the repository's root directory.

## Usage
Currently, there is no full-blown documentation, but the example config file in
`etc/example_session.yaml` gives a detailed insight on possible commands.

### Running the example the most simple way
After installation, you can run a simple example by calling the following command from outside the
repositories directory.
```
# leave the repository, e.g. by calling 'cd'
catmux_create_session $(python3 -m catmux.prefix)/share/catmux/example_session.yaml
```

To see further options, simply run it with argument `-h`:
```
$ catmux_create_session -h
usage: catmux_create_session [-h] [-n SESSION_NAME] [-t TMUX_CONFIG] [-d] [--overwrite OVERWRITE]
                             session_config

Create a new catmux session

positional arguments:
  session_config        Session configuration. Should be a yaml-file.

optional arguments:
  -h, --help            show this help message and exit
  -n SESSION_NAME, --session_name SESSION_NAME
                        Name used for the tmux session
  -t TMUX_CONFIG, --tmux_config TMUX_CONFIG
                        This config will be used for the tmux session
  -d, --detach          Start session in detached mode
  --overwrite OVERWRITE
                        Overwrite a parameter from the session config. Parameters can be specified
                        using a comma-separated list such as '--overwrite param_a=1,param_b=2'.
```

### Full blown example
To make use of all catmux features, run the following example command from outside the
repositories directory:
```
# leave the repository, e.g. by calling 'cd'
catmux_create_session $(python3 -m catmux.prefix)/share/catmux/example_session.yaml \
  --tmux_config $(python3 -m catmux.prefix)/share/catmux/tmux_default.conf \
  --session_name example_session \
  --overwrite show_layouts=True,replacement_param="new catmux user"
```

### Killing a catmux session
If you are not that familiar with tmux: To kill a session, simply type `tmux kill-session` in any
terminal window. In the `etc/tmux_default.conf` there is a key-binding for that, see
`etc/readme_tmux.txt` for details.

## Migrating from the catkin version of catmux
With the spread of ROS2, the need for a catkin-independent catmux has emerged.
Catmux is now a plain python package without the ROS integration.
Therefore, it is installed via pip and no longer needs to be part of a catkin workspace.
This opens the possibility to easily use catmux outside of robotics application, e.g. for server
administration or other development tasks.

Catmux no longer has the `package://<your_package_name>` lookup capabilities.
To achieve the same outcome, simply use rospack:
```
catmux_create_session $(rospack find <your_package_name>)/path/to/<your_catmux_session_config.yaml>
```

For ROS2, the same is achievable with `ros2 pkg prefix` but the yaml has to be installed (similar
to, for example, a launch file) and the installation path has to be specified:
```
catmux_create_session $(ros2 pkg prefix <your_package_name>)/path/to/the/installed/<your_catmux_session_config.yaml>

# for example: $ catmux_create_session $(ros2 pkg prefix catmux_test_pkg)/share/catmux_test_pkg/catmux_session.yaml
```
