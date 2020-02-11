# Introduction to Network Automation

Python example for generating configuration based on JSON or YAML input.

For an example of this application running in a Docker development environment, please see [Python Development with Docker and VSCode](https://bitbucket.org/packetflow/python-development-with-docker-and-vscode/src/master/)

## Configurator

The purpose of this sample project is to show the use of **Python and Jinja2** to generate network devices configuration from JSON or YAML input.

The Python script will ingest a data variable file (can be JSON or YAML format) and will render a configuration file based on a template in the `templates/` folder.

### Requirements

* Python 3.6
* [PyYAML](https://pypi.org/project/PyYAML/): Python YAML parser.
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/): Python template engine.

### Initialization

```shell
# clone code
git clone git@bitbucket.org:packetflow/introduction-to-network-automation.git
cd introduction-to-network-automation

# install virtualenv
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv

# create virtualenv
virtualenv -p /usr/bin/python3 venv
source ./venv/bin/activate

# install deps in virtualenv
pip3 install -r ./requirements.txt
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
