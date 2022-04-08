from cloudify import ctx

network_dictionary = {
  "us-west-1": "10.0.1.0/24",
  "us-west-2": "10.0.2.0/24",
  "us-east-1": "10.1.1.0/24",
  "us-east-2": "10.1.2.0/24",
}

# Look up the day in the node template's properties
network = ctx.node.properties['network']

# Set a runtime property on the node_instance that represents the abbreviation
ctx.instance.runtime_properties['subnet'] = network_dictionary[network]
