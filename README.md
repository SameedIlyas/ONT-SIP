##  Mininet
Download and run Mininet on a virtual machine or Linux-based device by following the instructions provided on https://mininet.org/download/, and verify its functionality using the guide at https://mininet.org/walkthrough/. Once it is set up and running, you can use the CLI to create topologies and connect remote controllers such as POX.

![Mininet (Pox)](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/542b539a-ae3f-4f6c-ba6b-106131413743)

![Mininet (Pox)(2)](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/eb6182ac-d6c9-4caf-9793-6f725e090a84)

## CustomTopo and POX firewall
The custom topology file can be run using the following command:  
~~~
sudo mn --custom custom --topo custom
~~~
For the Firewall to be immplemented using the Pox controller navigate to the directory where you have POX installed and run the POX controller specifying the path to the script as an argument. for example if it is saved as firewall-pox.py in the same directory, you can run the following code:  
~~~
./pox.py firewall-pox forwarding.l2_learning
~~~

## ONOS Installation
ONOS can be installed using the following github repository: https://github.com/jatj/sdn_onos/blob/master/INSTALL.md  
Once set up you can connect it with your topologies on mininet and acccess the ONOS GUI at http://localhost:8181/onos/ui where localhost is the local IP of your VM or device if you're using Linux.

![ONOS GUI](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/94b14ccc-515e-4e2e-aee9-0ff866f56c3a)

![ONOS GUI(topo)](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/fae059c2-78d3-41e1-8a2f-85d49bab0523)
 
## L2 Firewall using ACL rules
We will be setting up a layer 2 firewall by taking advantage of a pre-installed ONOS application called acl. An ACL or Access Control List is a list containing rules that are used to filter network traffic. We will be creating rules to deny traffic between certain hosts. First, start by activating the application from the ONOS CLI.  
~~~
karaf@root > app activate org.onosproject.acl
Activated org.onosproject.acl
~~~
This application exposes a REST API that allows us to add and remove rules and is available on http://local:8181/onos/v1/acl . The current active acl rules can be seen on http://local:8181/onos/v1/acl/rules.  
We can implement a firewall using the firewall.py script which blocks traffic between the MAC pairs present in the firewall-policies.csv, the delete_firewall.py script removes all ACL rules.  
Once the firewall.py script is run, the added rules can be viewed as such:  

![ACL](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/10c3b468-c4c6-4818-9b3e-a0235d3e2435)

The pingall will now block the connecctions mentioned in the CSV file.  

![Firewall](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/a3717829-8398-490f-b20f-a04dde558e7f)

![Firewall(2)](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/06b4f62f-ddb2-4c9c-ad45-a800f1a2f3fa)

![Firewall(3)](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/7452a3ee-dba4-43e1-b7b0-32ff0596e85b)

## VPLS Implementation
A subsytem called an Intent Framework will be utilized for this. Make sure you have the openflow app activated on ONOS. Set up a torus topology:  
~~~
sudo mn --topo torus,3,3 --mac --switch ovs,protocols=OpenFlow14  --controller remote,ip=172.17.0.2
~~~

![Torus](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/454fc907-859c-4c4d-926e-4848d113ca73)

Activate the vpls app:  
~~~
karaf@root > app activate org.onosproject.vpls
Activated org.onosproject.vpls
~~~
Define interface of each host:  
~~~
karaf@root > interface-add of:0000000000000101/1 h1
Interface added
karaf@root > interface-add of:0000000000000102/1 h2
Interface added
karaf@root > interface-add of:0000000000000203/1 h6
Interface added
~~~
Create a vpls and add each interface into it:  
~~~
karaf@root > vpls create vpls1
karaf@root > vpls add-if vpls1 h1
karaf@root > vpls add-if vpls1 h2
karaf@root > vpls add-if vpls1 h6
~~~
You can check the created intents by the vpls app fron the *Intents* view in the GUI.  

![Intents](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/bdaea223-ed80-48b7-8a96-17b6c8c6a0a9)

Break some links using the follwoing commands:  
~~~
mininet> link s1x3 s2x3 down
mininet> link s2x2 s2x3 down
~~~  
The intents will use different routes as per avaialability. The intents can be visualised by using the gui app and deactivating gui2 app.  

![Intents GUI](https://github.com/SameedIlyas/ONT-SIP/assets/127698326/68f1ef4b-a518-429c-b7c8-186acb74522d)












