# Introduction to Network Automation
This repo contains the code and files for the following:

* [Configurator](https://TBC) - Python example for generating configuration based on JSON or YAML input. 

* [Docker Developement Environment](https://TBC) - Docker files for creating a developement environment, and connecting to VSCode.

## Configurator

The purpose of this sample project is to show the use of **Python and Jinja2** to generate network devices configuration from JSON or YAML input.

The Python script will ingest a data variable file (can be JSON or YAML format) and will render a configuration file based on a template in the `templates/` folder.

### Requirements

- Python 3.6 or newer (preferably create a virtual environment, for information on creating a virtual environment -> [Python Virtual Environments a Primer](https://realpython.com/python-virtual-environments-a-primer/))
- [PyYAML](https://pypi.org/project/PyYAML/): Python YAML parser.
- [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/): Python template engine.

### Initialization

After you have created your python virtual environment you can clone and install the requirements.

```shell
git clone git@bitbucket.org:packetflow/introduction-to-network-automation.git
cd introduction-to-network-automation
pip install -r requirements.txt
```

### Example

Let's say we have the following variable file: `data/interfaces_vars.json`

```json
{
    "interfaces": [
        {
            "name": "Vlan177",
            "address": "10.77.1.68 255.255.255.0",
            "description": "Lan In-Band Network",
            "load_interval": 5
        },
        {
            "name": "Management1",
            "description": "lab01 - Eth100/1/37",
            "enabled": true,
            "address": "10.17.17.177 255.255.255.0",
            "load_interval": 5
        }
    ]
}
```

The script uses `sys.argv` to get the arguments from the command line and use it as parameters to denote the variables file location and the template file location. It then renders the template and data and creates a text file with the Cisco-based interface configuration.

Now lets run the script:

```shell
python3.6 configurator.py data/interfaces_vars.json templates/cisco_interfaces.j2
```

This will create a Cisco configuration file with the interfaces information.

```shell
!
interface Vlan177
  description NO DESCRIPTION
  ip address 10.77.1.68 255.255.255.0
  load-interval 5
!
interface Management1
  description lab01 - Eth100/1/37
  ip address 10.17.17.177 255.255.255.0
  load-interval 5
  no shutdown
!
!
```
---

## Docker Development Environment

There are 2 methods you can use to run the application inside a container-based development environment.
For this you will to have Docker installed, and if you want to follow the VS Code method you will Visual Studio Code and its extensions. See pre-requisites.

### Standalone container

You can build the `Dockerfile.standalone` image which will use the `continuumio/miniconda3` image, copy the projects files to `/app` directory in the container, with the execption of the paths indicated in the `.dockerignore` file, and install the project python dependencies.

**Procedure**:

- Clone repository

```shell
> git clone git@bitbucket.org:packetflow/introduction-to-network-automation.git
```

- Build Docker image

```shell
> cd introduction-to-network-automation
> docker build -t example/intro-netautomation:latest -f Dockerfile.standalone .
```

This will use the contents of `Dockerfile.standalone` to create the image. Don't forget the `.` at the end of the command!

- Spin up and connect to container

```shell
> docker run -it --name example01 example/intro-netautomation:latest
```

This will run and login into the container. You now have access to python, conda and project files under the `/app` directory.

**NOTE**: Work done on the container WILL be erased when you DELETE the container, but you don't have to worry to STOP the container - changes will still be there. That is why is highly recommended to use *git* or another SCM system to work with this type of project.

### VS Code Based Container

**Pre-Requisites**:

- Have [Remote-Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.
- And also recommended the [Docker extension](https://code.visualstudio.com/docs/azure/docker#_install-the-docker-extension) for managing the containers.

**Procedure**:

Using the [Visual Studio Code Editor](https://code.visualstudio.com/) you can automatically setup the docker development environment. You just have to do the following


- Clone the repository

```shell
> git clone git@bitbucket.org:packetflow/introduction-to-network-automation.git
```

- Open a new VS Code window and select **Remote-Containers: Open in a container**, and select the directory where the project was cloned.

This will launch a new window where it will show output of VS Code building the image with the specifications dictated on `Dockerfile` and the instructions on the `.devcontainer/devcontainer.json`.

By then you should have a fully functional development environment for this project.
