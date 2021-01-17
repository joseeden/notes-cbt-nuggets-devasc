
# 22 - Network Programmability and Network Automation Foundations #
________________________________________________________

<!-- 2021-01-14 01:47:21 -->

## WHY NETWORK AUTOMATION? ##

<p align=center>
    <img src="Images/network-automation.png">
</p>

1. **FASTER**
    Automation gets work done easier, faster.
    <br>
2. **STANDARDIZATION** 
    Standardize the network configurations acros the board.
    <br>
3. **KNOWN OUTCOMES** 
    You know what the en result is going to be.
    <br>
4. **MONITORING**  
    We can now collect daa specific/targetted to certaind evices quickly.
______________________________________________________________

**WHAT CAN YOU AUTOMATE?**

Normally, when we are faced with an option to change, we undergo these stages:

1. Shock            - Initial paralysis at hearing the bad news
2. Denial           - Trying to avoid the inevitable
3. Anger            - Frustrated outpouring of bottled-up emotion
4. Bargaining       - Seeking in vain for a way out 
5. Depression       - Final realization of the inevitable
6. Testing          - Seeking realistic solutions
7. Acceptance       - Finally finding the way forward

**Where to start?**

1.  **Monitoring**
    
    This is the safest way to start looking for stuff to automate.

    In the traditional method, we use SNMP for monitoring. 
    The drawback is SNMP sends more data than what is actually needed. 
    
    With automation, we can get specific data that we need when we need it.
    <br>

2.  **Device Provisioning**
    Biggest time-saver. With automation, we can update or provision resources with just a single script. There's going to be two components to this:
    <br>
    - **Template**      
        - Looks exactly like the CLI syntax, but with placeholders
        - normally use JINJA, python templating file
    <br>
    - **Config file**   
        - template will then go hand in hand with a device config file,
        - normally a YAML file
    <br>

3.  **Migration**
    This could be migrating between different Cisco models or migrating between completely different vendors.
    <br>
4.  **Config Management**
    There are a couple of concepts of configuration management.
    <br>

    - **Desired State**
        Managing the state of the configuration/s on the device/s.
        Here we are declaring a desired state for the network and we expect the network 
        to correct itself. if there's a drift from the desired state, we can take an action to 
        correct it.
    <br>

    - **Policies**
        We can implement policies and ran the policies against the config before we deploy a config to check if it violates any policies.
    <br>

5.  **Troubleshooting**
    Goes hand in hand with monitoring, you can easily run a script that checks the system.
    
    If you already know the possible scenarios which can cause issues, you can automate a sequence of actions specific to the issue and even resolve or 'heal' itself.

    An example set of steps:

        1. Detect failure
        2. Apply actually
        3. Monitor link
        4. Configure PBR - Policy-based routing

______________________________________________________________

## EVOLUTION OF APIs ##

Machines communicate through API. Just about every website has some sort of API.
<br>

1.  **PAST: SNMP**
    - Collect data from network devices. 
    - An agent running on the device reports back to a network management system - NMS 
    - Now, the data being sent by the device are specific to that device vendor.
    - Also, it's an all or nothing.
    - Either you get all the data back or you get no data back.
    - SNMPv3 also has security flaws.
    - SNMP also uses UDP - so it's not guaranteed, and not connection-oriented 
    <br>

2.  **PAST/PRESENT: CLI**
    - CLI won't be going anywhere. 
    - Through CLI, you can go to the device using either TELNET or SSH.
    <br>

3.  **PRESENT/FUTURE: NETCONF**
    - This is Network Configuration, came in 2006.
    - It sets out to replace SNMP.
    - Netconf works by sending data to and from a device using XML - structured data
    - The transport mechanism sits on top of SSH, so it can use port 22.
    - Since SSH is TCP, Netconf is connection-oriented.
    - It also uses RPC = REMOTE PROCEDURE CALLS
    - Basically, this uses pre-programmed commands to perform pre-program operations.
    <br>

4.  **PRESENT/FUTURE: REST API**
    - Rather than sending a pre-programmed command, we can send an HTTP GET request and specify in the URL the interface if we want to be more granular.
    - This performs the exact oepration as NETCONF but this uses HTTP or HTTPS.
______________________________________________________________

## NETWORK PROGRAMMABILITY vs NETWORK AUTOMATION ##

**NETWORK PROGRAMMABILITY**
Writing scripts that perform specific tasks for specific group of devices.

**NETWORK AUTOMATION**
Automation tools are for performing repeatable tasks against a large number of devices. Here we're declaring a desired state.

This is often referred to as *INTENT-BASED NETWORKING*
Declaring your intent on the network.

**ANSIBLE**
This is an automation and orchestration tool.

    AUTOMATION      - What we want to happen
    ORCHESTRATION   - When we want it to happen.

Ansible checks first if it needs to run the process before it takes an action. It is also written in Python

It is open-soruce and platform-agnostic - can run on any platform.

It is also AGENTLESS - no need to install anything on the network devices

It has MODULES - pre-built set of commands
______________________________________________________________

## DEVICES AND CONTROLLERS IN THE ERA OF SDN  ##

In the traditional network:

- Each device has a data plane and control plane
- Data plane        - this is where the data resides
- Control plane     - makes the decision where to send the data, brain of operations

In Software-defined network:

- Control plane is extracted and ou into one place. This is where you set all configurations.
- This CONTROLLER then distributes it to all devices.

