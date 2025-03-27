from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

# Define the topology
class SimpleTopo(Topo):
    def build(self):
        # Create 2 hosts and 1 router
        h1 = self.addHost('h1')
        h3 = self.addHost('h3')
        r2 = self.addSwitch('r2')  # Using a switch as a router in this case

        # Connect hosts to the router
        self.addLink(h1, r2)
        self.addLink(h3, r2)

# Create the network and start it
def createNetwork():
    topo = SimpleTopo()
    net = Mininet(topo=topo, controller=Controller)
    
    # Start the network
    net.start()

    # Open a CLI for interaction
    CLI(net)

    # Stop the network after use
    net.stop()

if __name__ == '__main__':
    # Set the log level to output information
    setLogLevel('info')
    createNetwork()

