#####################################################################################
#  Script that ingests data from YAML or JSON variables and renders the configuration
#  with a configuration template. Example
#
#  python configurator.py interface_vars.yaml cisco_intf_template.j2
#####################################################################################
import sys
import yaml
import json
import jinja2
from pathlib import Path


def main():
    # We will be using the sys.argv method to collect the arguments passed
    # Also to have the values as proper systems Paths and not worry about termination
    # based on filesystem, we are leveraging the Path object from pathlib
    variables_file = Path(sys.argv[1])
    template_file = Path(sys.argv[2])

    # Depeding on the file format, use the respective data ingestion library
    if variables_file.suffix in [".yml", ".yaml"]:
        with open(variables_file, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    elif variables_file.suffix == ".json":
        with open(variables_file, "r") as f:
            data = json.load(f)
    else:
        sys.exit(f"Not supported file format: {variables_file.suffix}")

    # Verify template format
    if template_file.suffix != ".j2":
        sys.exit(f"Template file format not supported: {template_file.suffix}")

    # Get the template data from file
    with open(template_file, "r") as f:
        template_data = f.read()

    # Generate template object
    template = jinja2.Template(template_data)

    # Render the template
    configuration_data = template.render(data)

    # Save the configuration to output file
    output_file = "data/conf.txt"
    with open(output_file, "w") as f:
        f.write(configuration_data)

    print("Created {} File! -->".format(output_file))
    print(configuration_data)
    return


if __name__ == "__main__":
    main()
