from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        self.fanout = fanout
        
        counterAgg = 0
        counterEdge = 0
        counterHost = 0
        # Create Core Switch
        c1 = self.addSwitch('c1')
        # Create Tree of Switches and Hosts
        for i in range(1,fanout+1):
            counterAgg += 1
            aggSwitch = self.addSwitch('a%s'%counterAgg)
            self.addLink(aggSwitch,c1,**linkopts1)
            for j in range(1,fanout+1):
                counterEdge += 1
                edgeSwitch = self.addSwitch('e%s'%counterEdge)
                self.addLink(edgeSwitch,aggSwitch,**linkopts2)
                for k in range(1,fanout+1):
                    counterHost +=1
                    host = self.addHost('h%s' % counterHost)
                    self.addLink(host,edgeSwitch,**linkopts3)
                    
                    
        print "Number of counterAgg = %s" % counterAgg
        print "Number of counterEdge = %s" % counterEdge
        print "Number of counterHost = %s" % counterHost
            
        

        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
