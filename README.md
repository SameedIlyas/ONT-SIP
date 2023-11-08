# Mininet
Download and run mininet on a VM or linux based device following the instructions on https://mininet.org/download/ and check the runnnings using https://mininet.org/walkthrough/.
Once set up and running, you can use the CLI to set up  topologies and can also connect remote controllers like POX.  

![WhatsApp Image 2023-11-08 at 22 09 24_d30a94d1](https://github.com/SameedIlyas/ONTInternship/assets/127698326/156f1fd7-8e56-41a9-a3eb-c1da8034ff89)  

![WhatsApp Image 2023-11-08 at 22 09 24_183f1384](https://github.com/SameedIlyas/ONTInternship/assets/127698326/c86739d3-a93a-4e96-92a7-8f7e8b4e9c3c)  

![WhatsApp Image 2023-11-08 at 22 09 25_4d0fa493](https://github.com/SameedIlyas/ONTInternship/assets/127698326/77ed4ef2-ac69-40ac-a8d1-01b9f5437b61)  


# Firewall in POX
The custom topology file can be run using the following command:  
~~~
sudo mn --custom custom --topo custom
~~~
For the Firewall to be immplemented using the Pox controller navigate to the directory where you have POX installed and run the POX controller specifying the path to the script as an argument. for example if it is saved as firewall-pox.py in the same directory, you can run the following code:  
~~~
./pox.py firewall-pox forwarding.l2_learning
~~~

# ONOS Installation
ONOS can be installed using the following github repository: https://github.com/jatj/sdn_onos/blob/master/INSTALL.md  
Once set up you can connect it with your topologies on mininet and acccess the ONOS GUI at http://localhost:8181/onos/ui where localhost is the local IP of your VM or device if you're using Linux.

![WhatsApp Image 2023-11-08 at 22 09 22_b911a2cf](https://github.com/SameedIlyas/ONTInternship/assets/127698326/604de73a-8308-4e09-a0aa-a6833c6dd261)  

![WhatsApp Image 2023-11-08 at 22 09 23_e18d5513](https://github.com/SameedIlyas/ONTInternship/assets/127698326/ac9e5fee-42eb-4236-9cde-b07377ed5560)  

# L2 Firewall using ACL rules
We will be setting up a layer 2 firewall by taking advantage of a pre-installed ONOS application called acl. An ACL or Access Control List is a list containing rules that are used to filter network traffic. We will be creating rules to deny traffic between certain hosts. First, start by activating the application from the ONOS CLI.  
~~~
karaf@root > app activate org.onosproject.acl
Activated org.onosproject.acl
~~~
This application exposes a REST API that allows us to add and remove rules and is available on http://local:8181/onos/v1/acl . The current active acl rules can be seen on http://local:8181/onos/v1/acl/rules.  
We can implement a firewall using the firewall.py script which blocks traffic between the MAC pairs present in the firewall-policies.csv, the delete_firewall.py script removes all ACL rules.  
Once the firewall.py script is run, the added rules can be viewed as such:  

![WhatsApp Image 2023-11-08 at 22 09 26_c49b5840](https://github.com/SameedIlyas/ONTInternship/assets/127698326/d9d6bd4b-841b-41a0-a94c-6cc10ff5f8c6)  

The pingall will now block the connecctions mentioned in the CSV file.  

![WhatsApp Image 2023-11-08 at 22 09 25_6c1c6591](https://github.com/SameedIlyas/ONTInternship/assets/127698326/0d7a5883-e4e9-4c18-8061-ae4befcdb30e)  

![WhatsApp Image 2023-11-08 at 22 09 25_0d03ad28](https://github.com/SameedIlyas/ONTInternship/assets/127698326/017841e5-7c9a-434b-9d80-ec504ca14dbb)  

![WhatsApp Image 2023-11-08 at 22 09 26_4f033619](https://github.com/SameedIlyas/ONTInternship/assets/127698326/09f84c0f-89a2-48c5-855d-22f78a146d2d)  


# VPLS Implementation
A subsytem called an Intent Framework will be utilized for this. Make sure you have the openflow app activated on ONOS. Set up a torus topology:  
~~~
sudo mn --topo torus,3,3 --mac --switch ovs,protocols=OpenFlow14  --controller remote,ip=172.17.0.2
~~~

![WhatsApp Image 2023-11-08 at 22 09 26_9f6e24f1](https://github.com/SameedIlyas/ONTInternship/assets/127698326/4c001083-dd42-4b65-a7f2-c6b0b51ffca0)  

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

![WhatsApp Image 2023-11-08 at 22 09 26_5159a0f5](https://github.com/SameedIlyas/ONTInternship/assets/127698326/0a99da7d-f06c-405e-b4b9-a475a455e63a)

Break some links using the follwoing commands:  
~~~
mininet> link s1x3 s2x3 down
mininet> link s2x2 s2x3 down
~~~  
The intents will use different routes as per avaialability. The intents can be visualised by using the gui app and deactivating gui2 app.  

![WhatsApp Image 2023-11-08 at 22 09 27_104be8ac](https://github.com/SameedIlyas/ONTInternship/assets/127698326/34fd36d7-5dc4-4877-9579-b4daeaf78825)











