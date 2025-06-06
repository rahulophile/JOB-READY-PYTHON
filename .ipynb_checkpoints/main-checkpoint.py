# -*- coding: utf-8 -*-
from fpdf import FPDF
import os
import sys
import re # Regex istemal karenge question number find karne ke liye

# --- POORA TEXT VARIABLE YAHAN HAI ---
copied_text = """
# Cloud Computing NPTEL Course - Compiled Questions and Answers

---

## Questions from Swayam Interface Screenshots

---

### Week 0: Assignment 0 (From Swayam Interface)

1)  Which software is usually used for network access control in an organizational network?
    ✅ a) Firewall
    b) Gateway
    c) Router
    d) Virus checker

2)  Which of the following is/are used for connectionless sockets?
    a) Datagram Socket only
    b) Datagram Packet only
    ✅ c) Both (i) and (ii)
    d) None of these

3)  Which of the following is most appropriate about Threads? Threads of a process share
    a) only global variables.
    b) only heap.
    c) neither global variables nor heap.
    ✅ d) both heap and global variables.

4)  What is the maximum number of hosts under class B addresses?
    a) 65536
    ✅ b) 65534
    c) 65535
    d) 254

5)  Consider a system with 2 level caches. The access times of Level 1 cache, Level 2 cache, and main memory are 1 ns, 10ns, and 400 ns, respectively. The hit rates of Level 1 and Level 2 caches are 0.8 and 0.9, respectively. What is the average access time of the system, ignoring the search time within the cache?
    a) 12.6 ns
    b) 11.2 ns
    ✅ c) 10.6 ns
    d) 12.4 ns

6)  Using a larger block size in a fixed block size file system leads to
    ✅ a) better disk throughput but poorer disk space utilization
    b) better disk throughput and better disk space utilization
    c) poorer disk throughput but better disk space utilization
    d) poorer disk throughput and poorer disk space utilization

7)  Transport layer is implemented in the NIC of a typical computer system.
    a) True
    ✅ b) False

8)  A computer's processor sends 32 bit addresses to the cache controller. It has a 512 KByte, 8-way set associative, write back data cache with block size of 32 Bytes. In addition to the address tag, each cache tag directory entry contains 3 valid bits and 1 modified bit. Find the size of the cache tag directory.
    a) 212 Kbits
    ✅ b) 160 Kbits
    c) 320 Kbits
    d) 120 Kbits

9)  Flow control is mainly implemented in
    a) Physical Layer
    b) Application Layer
    ✅ c) Transport Layer
    d) Session Layer

10) Where does the swap space reside?
    a) RAM
    ✅ b) Disk
    c) ROM
    d) On-chip cache

---

### Week 1: Assignment 1 (From Swayam Interface)

1)  Which of the following fall(s) under the "essential characteristics" of cloud computing?
    ✅ A. Resource Pooling
    ✅ B. Measured Service
    ✅ C. Rapid Elasticity
    d. Latency

2)  "Google Slide" is an example of
    a. PaaS
    b. IaaS
    ✅ c. SaaS
    d. FaaS

3)  Which of the following is/are public cloud platform(s)?
    a. Windows Server Hyper-V
    b. Google Cloud Interconnect
    c. Amazon Virtual Private Cloud
    ✅ d. Microsoft Azure

4)  VM technology allows multiple virtual machines to run on a single physical system.
    ✅ a. True
    b. False

5)  Which one of the following is/are disadvantage(s) of cloud computing?
    a. Resource pooling
    ✅ b. It requires an always-on internet connection.
    c. Ubiquitous
    d. On-demand payment policy

6)  For less data-intensive applications, horizontal scale-out elasticity is the ideal solution.
    a. True
    ✅ b. False

7)  The combination of Service-Oriented Infrastructure and Cloud Computing realizes to ______
    a. FTP
    b. SNTP
    ✅ c. XaaS
    d. FaaS

8)  What is/are the main requirement(s) of a Cloud Service Provider (CSP)?
    ✅ a. Increase agility
    b. Increase cost
    ✅ c. Increase productivity
    d. Decrease cost

9)  PaaS (Platform as a Service) brings the benefits: (i) Creation of software (ii) Integration of web services and databases
    a. Only (i)
    b. Only (ii)
    ✅ c. Both (i) and (ii)
    d. Neither (i) nor (ii)

10) A ______ is a distributed computer system that consists of a collection of interconnected stand-alone computers working together as an integrated computing resource.
    a. Grid
    ✅ b. Cluster
    c. Cloud
    d. Node

---

### Week 2: Assignment 2 (From Swayam Interface)

1)  The public cloud has a risk of multi-tenancy.
    ✅ A. True
    B. False

2)  Ubuntu Enterprise Cloud (UEC) is an example of
    ✅ A. Private cloud
    B. Public cloud
    C. Hybrid cloud
    D. Community Cloud

3)  Organization should consider-(i) Network Dependency and (ii) Risks from multi-tenancy while thinking of deploying an outsourced private cloud.
    A. Only (i)
    B. Only (ii)
    ✅ C. Both (i) and (ii)
    D. None of (i) and (ii)

4)  Which of the following is/are XML parser API(s)?
    A. XaaS (Anything as a Model)
    ✅ B. DOM (Document Object Model)
    C. CLI (Command Line Interface)
    D. SLA (Service Level Agreement)

5)  What is/are the main difference(s) between virtualization and dual boot?
    A. No difference between dual boot and virtualization.
    B. In virtualization, operating systems are not isolated from each other, but not in dual boot.
    C. In a dual boot, both operating systems run simultaneously, but not in virtualization.
    ✅ D. In virtualization, both operating systems run simultaneously, but not in dual boot.

6)  In virtualization, a virtual machine monitor is also called
    ✅ A. Hypervisor
    B. Short-term Scheduler
    C. Analyzer
    D. Parser

7)  Speed and flexibility are the two disadvantages of hardware-assisted virtualization.
    ✅ A. True
    B. False

8)  The following problems are addressed through Web services:
    ✅ A. Firewall
    ✅ B. Interoperability
    ✅ C. Complexity
    D. Speed

9)  A web service can be discovered using
    A. SMS
    B. HTTP
    C. SMTP
    ✅ D. UDDI

10) Service-Oriented Architecture (SOA) consists of relationships between:
    A. Two entities ( a service provider and a requestor)
    B. Two entities ( a service provider and a broker)
    ✅ C. Three entities ( a service provider, a service requestor, and a broker)
    D. Three entities ( a service provider, a service requestor, and a hypervisor)

---

### Week 3: Assignment 3 (From Swayam Interface)

1)  Which of the following is/are NOT SLA requirement(s) of PaaS cloud delivery model?
    a. Privacy
    ✅ b. Data Retention and Deletion
    ✅ c. Machine-Readable SLAs
    d. Certification

2)  Which of the following is/are true regarding penalty cost? (Here D(t) and R(t) are instantaneous demand and resources at time t.)
    a. Penalty cost ∝ ∫|D(t)/R(t)|dt
    ✅ b. If demand is flat, penalty is equal to 0.
    c. If demand is exponential (D(t)=e^t), any fixed provisioning interval (tp) according to the current demands will fall linearly behind.
    ✅ d. The penalty cost for exponential demand is exponential.

3)  Row-oriented storage is efficient for data-warehouse workloads.
    a. TRUE
    ✅ b. FALSE

4)  Which of the following is/are example(s) of cloud SLA(s) with IaaS delivery model?
    ✅ a. Amazon EC2
    b. Google App Engine
    c. Salesforce CRM
    d. Zoho mail

5)  Which of the following OpenStack components is used for block storage services?
    a. Keystone
    ✅ b. Cinder
    c. Swift
    d. Neutron

6)  In cloud, service downtime is 30 minutes and availability of the service is 0.80. What is the service uptime?
    (a) 120 minutes
    (b) 60 minutes
    ✅ (c) 150 minutes
    (d) 135 minutes

7)  In Google File System (GFS), the master maintains regular communication with the chunk servers.
    ✅ a. TRUE
    b. FALSE

8)  What is/ are the expected SLA parameters for Software-as-a-Service (SaaS):
    ✅ (a) Reliability
    ✅ (b) usability
    (c) Cache Memory size
    ✅ (d) Customizability

9)  Which of the following option(s) is/are correct?
    ✅ a. Service Level Agreement(SLA) contains Service Level Objectives(SLO)
    b. Service Level Objectives(SLO) contains Service Level Agreement(SLA)
    c. Multiple Service Level Agreements (SLAs) are aggregated to Key Performance Indicator (KPI)
    ✅ d. Key Performance Indicators (KPIs) are aggregated to Service Level Objectives(SLO)

10) Statement 1: In OpenStack block storage, the stored objects persist until the VM is terminated. Statement 2: In OpenStack ephemeral storage, the stored objects are accessible from within VM as local file system.
    a. Both statement 1 and 2 are correct
    b. Statement 1 is correct and statement 2 is incorrect
    ✅ c. Statement 2 is correct and statement 1 is incorrect
    d. Both statement 1 and 2 are incorrect

---

### Week 4: Assignment 4 (From Swayam Interface)

1)  In Google Cloud Platform (GCP), Cloud Datastore provides flexible object storage with global edge caching.
    (a) TRUE
    ✅ (b) FALSE

2)  Match the following columns:
    A. Cinder, OpenStack | 1. MySQL or NoSQL databases.
    B. GoogleAPIs | 2. Google's fully managed, petabyte scale, low cost analytics data warehouse to find meaningful insights.
    C. Cloud SQL | 3. Integrate Google's services into the application.
                       | 4. Manages block storage in OpenStack.
    Choose the correct option:
    ✅ a) A-4, B-3, C-1
    b) A-1, B-3, C-2
    c) A-2, B-4, C-1
    d) A-3, B-1, C-2

3)  Statement 1: Azure supports public cloud platform. Statement 2: Azure App Service plan defines security.
    ✅ (a) Statement 1 is True and Statement 2 is False
    (b) Statement 1 is False and Statement 2 is True
    (c) Both are True
    (d) Both are False

4)  Which of the following components of OpenStack is responsible for providing persistent block storage to running instances
    (a) Nova
    ✅ (b) Cinder
    (c) Swift
    (d) None of the above

5)  Which of the following is/are App services provided by Google Cloud Platform?
    ✅ (a) BigQuery
    (b) Google App Engine
    ✅ (c) Cloud Endpoints
    (d) Cloud SQL

6)  Which of the following is/are App Services provided Google Cloud Platform?
    ✅ (a) Big Query
    ✅ (b) Cloud App Engine
    (c) Cloud Endpoints
    ✅ (d) Cloud SQL

7)  Google Cloud End Points helps to:
    a) migrate the web app to Google Cloud Platform.
    ✅ b) scale up the app according to the demand/ service requests.
    c) provide flexible object storage with global edge caching.
    d) Integrate Google's services into the application.

8)  The Azure App plan has a scale count of ______ instances.
    (a) 1 to 50
    ✅ (b) 1 to 20
    (c) 1 to 10
    (d) 1 to 100

9)  Match the following columns regarding OpenStack:
    Column 1 | Column 2
    ------- | --------
    A. Ephemeral storage | 1. Cinder
    B. Block storage | 2. Nova
    C. Object storage | 3. Swift
    (a) A-1, B-2, C-3
    (b) A-2, B-3, C-1
    (c) A-3, B-1, C-2
    ✅ (d) A-2, B-1, C-3

10) In GCP, "gcloud app browse" - can be used to start the local development server for the application.
    (a) TRUE
    ✅ (b) FALSE

---

### Week 5: Assignment 5 (From Swayam Interface)

1)  Multiple KPIs are aggregated to SLA.
    A. TRUE
    ✅ B. FALSE

2)  Statement I: In resource management, resource allocation is the allocation of a service provider's resources to a customer Statement II: Resource mapping is correspondence between resources required by the users and resources available with the provider. Which of the options is/are correct?
    A. Statement I is TRUE and Statement II is FALSE
    ✅ B. Statement I is FALSE and Statement II is TRUE
    C. Both statements are TRUE
    D. Both statements are FALSE

3)  A third party application runs in the cloud for 12 hours/day. At the end of one month [30 days], it was found that the cloud service suffered 5 outages of durations: 1 hour 30 minutes, 30 minutes, 2 hours 15 minutes, 1 hour 45 minutes and T hours, each on different days over the service period. Suppose a cloud guarantees service availability for 97% of time. What are the possible value(s) of T that SLA negotiation gets honored in terms of service availability?
    ✅ A. 3 hours
    B. 6 hours
    C. 12 hours
    D. 8 hours

4)  In a MapReduce framework, the HDFS block size is 64 Mb. We have 3 files of size 65 Kb, 64 Mb and 128 Mb. How many input splits will be created by the Hadoop framework?
    A. 2
    B. 3
    ✅ C. 4
    D. 5

5)  What is/are the correct statement(s) regarding VM load management?
    ✅ A. When load increases, new VMs should be scheduled to new nodes.
    B. When load decreases, use WOL to start up waiting nodes.
    ✅ C. When load increases, use WOL to start up waiting nodes.
    ✅ D. When load decreases, live migrate VMs to more utilized nodes.

6)  Which of the following is/are the objective(s) of Resource Management?
    ✅ A. Improved Quality of Service (QoS)
    ✅ B. Scalability
    C. Increased overhead
    ✅ D. Increased throughput

7)  The correct statement(s) for necessary and sufficient conditions for the detection of inheritance conflict is/are:
    A. Sufficient condition: current entry role and at least one exit role forms conflicting pair
    ✅ B. Sufficient condition: current entry role is senior to at least one exit role
    C. Necessary condition: current entry role is senior to at least one exit role
    ✅ D. Necessary condition: at least one exit role

8)  Which of the following part(s) of the MapReduce is responsible for processing one or more chunks of data and producing the output results?
    A. Mapper
    B. Reducer
    ✅ C. Map task
    D. Task execution

9)  Consider that the peak computing demand for an organization is 200 units. The demand as a function of time can be expressed as D(t) = 3(1+t). Baseline (owned) unit cost is 120 and cloud unit cost is 125. Cloud is costlier than owning for a period of 150 time units.
    ✅ A. TRUE
    B. FALSE

10) Which of the following is/are resource provisioning approaches?
    A. Intelligent multi-agent model
    ✅ B. Network queueing model
    ✅ C. Adaptive resource provisioning
    D. Reinforcement learning guided control policy

---

### Week 6: Assignment 6 (From Swayam Interface)

1)  Modification threat on cloud security is an example of:
    ✅ A. Deception
    B. Disclosure
    ✅ C. Disruption
    ✅ D. Usurpation

2)  Which of the following is/are example(s) of passive attack?
    A. Replay
    B. Denial of service
    ✅ C. Traffic analysis
    D. Masquerade

3)  Interception is an attack on integrity
    A. TRUE
    ✅ B. FALSE

4)  Statement I: Intrusion Detection System (IDS) scans the incoming messages, and creates alerts when suspected scans/attacks are in progress. Statement II: Authentication is the identification of legitimate users.
    A. Statement I is TRUE and statement II is FALSE.
    B. Statement I is FALSE and statement II is TRUE.
    ✅ C. Both statements are TRUE.
    D. Both statements are FALSE.

5)  Match the following attacks with their descriptions:
    1. Injection attack | (a) Attacker sending huge amounts of requests to a certain service and causing denial of service.
    2. Flooding | (b) Browser-based security issues.
    3. Metadata (WSDL) spoofing attack | (c) Introduce malicious code to change the course of execution.
                                    | (d) Malicious reengineering of Web Services' metadata description.
    A. 1-(a), 2-(b), 3-(d)
    ✅ B. 1-(c), 2-(a), 3-(d)
    C. 1-(b), 2-(c), 3-(d)
    D. 1-(a), 2-(c), 3-(d)

6)  Recovery Time Objective (RTO) represents the period of time allowed for the complete execution of the task.
    A. TRUE
    ✅ B. FALSE

7)  The correct statement(s) for necessary and sufficient conditions for the detection of inheritance conflict is/are:
    A. Sufficient condition: current entry role and at least one exit role forms conflicting pair
    ✅ B. Sufficient condition: current entry role is senior to at least one exit role
    C. Necessary condition: current entry role is senior to at least one exit role
    ✅ D. Necessary condition: at least one exit role

8)  Which of the following is/are hypervisor risks associated with VM escape?
    ✅ A. Vulnerable virtual machine applications like Vmchat, VMftp, Vmcat etc.
    B. Rogue hypervisor that hides itself from normal malware detection systems
    ✅ C. Improper configuration of VM
    D. Rogue hypervisor that creates a covert channel to dump unauthorized code

9)  In fault tolerance, replication is the duplication of critical components of a system with the intention of increasing reliability of the system, usually in the case of a backup or fail-safe.
    A. TRUE
    ✅ B. FALSE

10) Which of the following Open-source tools is/are used for retrieving web pages in Amazon EC2 platform?
    ✅ A. wget
    B. hping
    C. ifconfig
    D. nmap

---

### Week 7: Assignment 7 (From Swayam Interface)

1)  Which of the following options is correct about geographic information? Statement 1: Geographic information could be static or dynamic. Statement 2: Geographic information varies in scale Statement 3: Population of a city/town is a static geographic information
    ✅ a. Statement 1 & 2 are True, but Statement 3 is False.
    b. Statement 2 & 3 are True, but Statement 1 is False.
    c. Statement 1& 3 are True, but Statement 2 is False.
    d. All the statements are True.

2)  Which of the following is true about geographical information system? Choose the most appropriate option.
    a) Variable load of the GIS server needs dynamic scaling of resources.
    b) GIS uses network intensive web services.
    c) GIS requires a high level of reliability.
    ✅ d) All of these.

3)  Which of the following is/are not a benefit of Fog computing ?
    a. Location awareness
    b. Improved QoS
    ✅ c. High latency
    ✅ d. Man-in-the-middle-attack

4)  Which of the following statements is false about Code offloading using cloudlet? Statement 1: The architecture reduces latency by using multi-hop network. Statement 2: It potentially lowers battery consumption by using short range radio.
    a. Statement 1 is correct but Statement 2 is incorrect
    ✅ b. Statement 2 is correct but Statement 1 is incorrect
    c. Both the statements are correct
    d. Both the statements are incorrect.

5)  Which of the following are some of the key components of Mobile cloud computing ? Choose the most appropriate option.
    a. Solver
    b. Synchronizer
    c. Profiler
    ✅ d. All of the above

6)  Which of the following statement(s) is/are FALSE about Fog Computing?
    ✅ a. Intelligence is brought to the cloud from the end users.
    b. Fog computing is used for real-time applications
    ✅ c. Fog nodes' response time is much higher than cloud server
    ✅ d. Network routers, WiFi Gateways will not be capable of running applications

7)  Fog computing enablers are
    ✅ a. Virtualization
    b. Big data
    ✅ c. Service oriented architecture
    d. None of these

8)  Which of the following is/are feature(s) of Mobile Cloud Computing?
    ✅ a) Use less mobile device resources because applications are cloud-supported
    b) Reduce reliability with information backed up and stored in the cloud
    ✅ c) Mobile devices connect to services delivered through an API architecture
    d) Facilitates slower development, delivery and management of mobile apps

9)  Which of the following is/are the challenge(s) of Geospatial Cloud?
    ✅ a) Scaling of Spatial Databases
    ✅ b) Policy management among the tenants
    ✅ c) Implementation of Spatial Databases
    d) None of the above

10) Consider following statements: Statement 1: Geospatial Cloud helps to integrate data from heterogeneous back-end data service. Statement 2: Data services can be inside and/or outside of the cloud environment in Geospatial Cloud.
    a. Statement 1 is Correct, but Statement 2 is Incorrect.
    b. Statement 2 is Correct, but Statement 1 is Incorrect.
    ✅ c. Both statements are Correct.
    d. Both statements are Incorrect

---

### Week 8: Assignment 8 (From Swayam Interface)

1)  Which of the following statements is/are true about Docker ? Statement 1: Docker hub is used for building docker images and creating docker containers. Statement 2: Docker compose is a registry used to host various docker images.
    a. Statement 1 is correct but Statement 2 is incorrect
    b. Statement 2 is correct but Statement 1 is incorrect
    c. Both the statements are correct
    ✅ d. Both the statements are incorrect.

2)  Virtual machines take up less space than Containers.
    a. True
    ✅ b. False

3)  Which of the following statements is/are correct? Choose the most appropriate option. Statement 1: An image is a light weight, stand alone, executable package that includes everything to run a piece of software. Statement 2:Container is a run time instance of an image.
    a. Statement 1 is correct but Statement 2 is incorrect
    b. Statement 2 is correct but Statement 1 is incorrect
    ✅ c. Both the statements are correct
    d. Both the statements are incorrect.

4)  In IoT based vehicular data clouds, vehicles providing their networking and data processing capabilities to other vehicles through the cloud is best identified with which of the following services?
    a. SaaS
    b. PaaS
    ✅ c. IaaS
    d. BaaS

5)  Each container can not run as an isolated process in user space.
    a. True
    ✅ b. False

6)  Containers can share the OS kernel with other containers.
    ✅ a. True
    b. False

7)  For sensor resources that do not have direct connection to the cloud, sensor network proxy provides the connection.
    ✅ a) True
    b) False

8)  An IoT platform has following basic building blocks
    ✅ (a) Things
    ✅ (b) Gateway
    ✅ (c) Network and Cloud
    (d) Learning Module

9)  In the context of Green Cloud Computing, the Power Usage Effectiveness is defined as
    a. Power Delivered / Overall Power
    ✅ b. Overall Power / Power Delivered
    c. Overall Power * Power Delivered
    d. None of these

10) A green broker can perform scheduling of applications to reduce energy consumption.
    ✅ a. True
    b. False

---

### Week 9: Assignment 9 (From Swayam Interface)

1)  Which of the following statements is/are false ?
    ✅ a. Fog and Edge computing are substitutes for cloud computing.
    b. Fog and Edge computing may aid cloud computing in overcoming some of the limitations like latency issues.

2)  Which of the following is not a layer of the Cloud-Fog environment model?
    a. Client layer
    ✅ b. Serverless layer
    c. Fog layer
    d. Cloud layer

3)  In the Cloud-Fog environmental model, servers contain a fog server manager and virtual machines to manage requests by using ______ technique.
    a. Image virtualization
    b. Container virtualization
    ✅ c. Server virtualization
    d. None of these

4)  The architecture used for resource management in fog/edge computing is classified on the basis of which of the following?
    ✅ a. Tenancy
    ✅ b. Data flow
    c. Hardware
    d. All of these

5)  Which of the following underlying algorithm(s) is used to facilitate fog/edge computing ?
    ✅ a. Discovery
    ✅ b. Load balancing
    ✅ c. Benchmarking
    d. Cache Flow

6)  ______ is a technique in which a server, an application and the associated data are moved onto the edge of the network
    a. Containerization
    b. Virtualization
    ✅ c. Offloading
    d. None of these

7)  Cloud federation is the collaboration between cloud service providers to achieve which of the following? Choose the most appropriate option(s).
    ✅ a. Capacity utilization
    ✅ b. Interoperability
    c. Offloading
    d. None of these

8)  Which of the following is false about loosely coupled federations?
    a. Limited inter operations between cloud instances.
    b. Usually no support for advanced features.
    ✅ c. Advanced control over remote resources.
    d. None of these

9)  In which of the following different CSPs establish an agreement stating the terms and conditions under which one partner cloud can use resources from another.
    a. Loosely coupled federation
    ✅ b. Partially coupled federation
    c. Tightly coupled federation
    d. All of these

10) Hybrid architecture combines the existing on-premise infrastructure (usually a private cloud) with remote resources from one or more public clouds to provide extra capacity to satisfy peak demand periods.
    ✅ a. True
    b. False

---

### Week 10: Assignment 10 (From Swayam Interface)

1)  VM migration is the process of moving running applications or VMs from one physical host to another host.
    ✅ a. True
    b. False

2)  Given the VM memory size of 1024GB and the transmission rate of 16 MB/sec What are the total migration time and downtime for non-live VM migration? Choose the most appropriate option.
    a. 20 hours, 25 hours
    ✅ b. 18 hours, 18 hours
    c. 16 hours, 16 hours
    d. 24 hours, 20 hours

3)  With Docker, the resource management effort is separated from the configuration effort.
    ✅ a. True
    b. False

4)  In Docker utility, ______ is a collection of filesystem layers and some metadata which, if taken together, can be spun up as Docker containers.
    a. Operating System
    b. Microservice
    c. Virtual Machine
    ✅ d. Image

5)  What is(are) the reason(s) to opt for VM migration in the cloud computing paradigm?
    a. No particular reason; depends on the will of the end client/user.
    ✅ b. To remove a physical machine from service
    c. To save power consumption
    ✅ d. To relieve the load on the congested hosts.

6)  What is(are) the key advantage(s) of Docker?
    ✅ a. It facilitates microservice architecture
    ✅ b. It can be used to package software
    ✅ c. It can be used to model networks.
    d. None of these

7)  Post-copy and Pre-copy migration approaches are followed in :
    ✅ a. Live Migration process
    b. Non-live Migration process
    c. Hybrid Migration process
    d. None of these

8)  Which of the following is (are) true in the case of Docker architecture? Statement-1: Private Docker registry is a service that stores Docker images. Statement-2: Docker on the host machine is split into two parts- a daemon with a RESTful API and a client who talks with the daemon.
    a. Only Statement-1 is true
    b. Only Statement-2 is true
    ✅ c. Both Statement-1 and 2 are true
    d. Neither Statement 1 nor 2 is true

9)  Which of the statement(s) is (are) true for containers? Statement-1: Docker is an open platform for automating the deployment, scaling, and management of containerized applications. Statement-2: Containers make it easy to share CPU, memory, storage and network resources at the operating system level.
    a. Only Statement-1 is true
    ✅ b. Only Statement-2 is true
    c. Both Statement-1 and 2 are true
    d. Neither Statement 1 nor 2 is true

10) Kubernetes operates at the hardware level.
    a. True
    ✅ b. False

---

### Week 11: Assignment 11 (From Swayam Interface)

1)  Which of the following statements is/are false ?
    ✅ a. Serverless computing allows the users with more control over the deployment environment compared to PaaS.
    b. Serverless computing is a form of cloud computing that allows users to run event driven granular applications.

2)  Which of the following options is most appropriate for FaaS ? Statement 1: Each function in the Faas platform gets unlimited execution time. Statement 2: Functions are always active and ready for execution.
    a. Statement 1 is correct but Statement 2 is incorrect.
    b. Statement 2 is correct but Statement 1 is incorrect.
    c. Both the statements are correct.
    ✅ d. Both the statements are incorrect.

3)  AWS S3 is a fully managed proprietary NoSQL database service that supports key-value and document data structures and is offered by Amazon.com as part of the Amazon Web Services portfolio.
    a. True
    ✅ b. False

4)  BigQuery is a fully-managed, serverless data warehouse by ______.
    a. AWS
    ✅ b. Google
    c. Microsoft
    d. IBM

5)  AWS charges for the provisioned resources and executing Lambda.
    a. True
    ✅ b. False

6)  In serverless computing the user has to manage the scalability needs of a function, unlike FaaS.
    a. True
    ✅ b. False

7)  Which of the following is/are the goal of sustainable cloud computing? Choose the most appropriate option.
    ✅ a. Minimizing the energy consumption.
    ✅ b. Increasing reliability of CDCs.
    ✅ c. Minimizing carbon footprint related cost.
    d. Increasing network traffic

8)  Which of the following is not a category of research initiative on sustainable cloud computing?
    a. Renewable Energy
    b. Capacity planning
    ✅ c. Environment Sandboxing
    d. None of these

9)  CDCs consist of a chassis and racks to place the servers to process the IT workloads.
    ✅ a. True
    b. False

10) ______ are an important distribution mechanism for libraries and custom runtimes in AWS serverless ecosystem.
    a. Runtimes
    ✅ b. Lambda Layers
    c. Log streams
    d. None of these

---

### Week 12: Assignment 12 (From Swayam Interface)

1)  The key features of Mobile Cloud Computing (MCC) for 5G networks include
    ✅ a. Reliability improvement
    ✅ b. Sharing of resources
    ✅ c. Offloading data processing
    d. Mitigating network traffic congestion

2)  Cyber-physical system is all about ______ of the physical and the cyber.
    a. Union
    ✅ b. Intersection
    c. Segregation
    d. None of above

3)  Cloud computing services provide a flexible platform for realizing the goals of Cyber-Physical systems.
    ✅ a. True
    b. False

4)  The advantage(s) of Cyber-Physical Cloud Computing is(are) as follows
    ✅ a. Modular composition
    b. Multi-Tenancy
    c. Data flow
    ✅ d. Reliability and resiliency

5)  A______ is a trace generated by a moving object in geographical space, usually represented by a series of chronologically ordered points.
    a. Time series
    b. Road map
    ✅ c. Spatial trajectory
    d. Spatial crowdsourcing

6)  Limitation(s) of IoT devices is(are)
    a. Containerization
    ✅ b. Storage
    ✅ c. Processing
    ✅ d. Power requirement

7)  Which of the statements is(are) true with respect to Spatial cloud Statement 1: It does not support shared resource pooling which is useful for participating organizations with common or shared goals Statement 2: Spatial cloud provides infrastructure requirement that is based on application, with nothing to purchase. This leverages the scalability of the application.
    a. Only statement 1 is true
    ✅ b. Only statement 2 is true
    c. Both statements are true
    d. None of the statements is true

8)  Customized wearable devices for collecting health parameters are the best examples of
    a. IoHT
    b. Fog device
    c. Fog-Cloud interfaced.
    ✅ d. Cloud-Fog-Edge-IoHT

9)  The cyber-physical system involves transdisciplinary approaches, merging the theory of cybernetics, mechatronics, design, and process science.
    ✅ a. True
    b. False

10) 5G network technology has proven to offer a theoretical download speed of 1Gbit/s.
    a. True
    ✅ b. False

---
---

## Questions from Official NPTEL Solution Pages

---

### Assignment-Week 1 (Official Solutions)

1)  Which of the following fall(s) under the “essential characteristics” of cloud computing?
    ✅ A. Resource Pooling
    ✅ B. Measured Service
    ✅ C. Rapid Elasticity
    D. Latency
    *(Correct Answer: A,B,C)*

2)  "Google Doc" is an example of
    A. PaaS
    B. IaaS
    ✅ C. SaaS
    D. FaaS
    *(Correct Answer: C)*

3)  Business-Process-as-a-Service is not a part of XaaS.
    A) True
    ✅ B) False
    *(Correct Answer: B)*

4)  Network Function Virtualization involves the implementation of __________ function in software that can run on a range of industry-standard servers __________.
    A. network,software
    B. hardware, software
    C. hardware, network
    ✅ D. network,hardware
    *(Correct Answer: D)*

5)  Which are the following applications for SaaS (Software as a Service) architecture?
    ✅ A) Billing software
    ✅ B) CRM
    C) App engines
    D) None of above
    *(Correct Answer: A,B)*

6)  Web access to commercial software is one of the SaaS characteristics in the cloud computing paradigm.
    ✅ A. True
    B. False
    *(Correct Answer: A)*

7)  In the case of the client-server model: Statement (i) Virtualization is a core concept; Statement (ii) system can scale infinitely
    A) Only Statement (i) is correct
    B) Only Statement (ii) is correct
    C) Both Statements (i) and (ii) are correct
    ✅ D) None of the statements is correct
    *(Correct Answer: D)*

8)  Client-server model is always load-balanced
    A) True
    ✅ B) False
    *(Correct Answer: B)*

9)  PaaS (Platform as a Service) brings the benefits: (i) Creation of software (ii) Integration of web services and databases
    A. Only (i)
    B. Only (ii)
    ✅ C. Both (i) and (ii)
    D. Neither (i) nor (ii)
    *(Correct Answer: C)*

10) Which of the following is false?
    a) Private cloud is dedicated solely to an organization.
    ✅ b) Community cloud is a composition of public and private cloud.
    c) Public cloud is available to the general public.
    d) None of these
    *(Correct Answer: b)*

---

### Assignment-Week 2 (Official Solutions)

1)  Service-Oriented Architecture (SOA) possess:
    ✅ a) A service provider, service requestor and service broker
    b) A service provider and service requestor
    c) A service requestor and service broker
    d) Only a service broker
    *(Correct Option: A)*

2)  XML is designed to describe ______
    a) pricing
    b) SLA
    ✅ c) data
    d) service
    *(Correct Option: C)*

3)  SOAP (Simple Object Access Protocol) does not restrict the endpoint implementation technology choices. SOAP is a platform-neutral choice.
    ✅ a) True
    b) False
    *(Correct Option: A)*

4)  A Cyber-Physical Cloud Computing (CPCC) architectural framework is a ______ environment that can rapidly build, modify and provision cyber-physical systems composed of a set of ______ based sensor, processing, control, and data services.
    ✅ a) system, cloud computing
    b) cloud computing, system
    c) system, edge computing
    d) edge, system computing
    *(Correct Answer: A)*

5)  Network Virtualization is a ______ environment that allows ______ service providers to dynamically compose ______ virtual networks.
    a) networking, single, single
    b) physical, single, multiple
    c) networking, multiple, single
    ✅ d) networking, multiple, multiple
    *(Correct Option: D)*

6)  Customized wearable devices for collecting health parameters are the best examples of
    a) IoHT
    b) Fog device
    c) Fog-Cloud interfaced.
    ✅ d) Cloud-Fog-Edge-IoHT
    *(Correct Answer: d)*

7)  Dew Computing is a paradigm where on-premises computers provide functionality that is ______ of cloud services and is also collaborative with cloud services
    a) dependant
    ✅ b) independent
    c) partial dependant
    d) none of these
    *(Correct Option: B)*

8)  SOAP uses ______ as transport protocol
    a) UDDI
    b) SLA
    ✅ c) HTTP
    d) XML
    *(Correct Answer: c)*

9)  Virtual Machine Monitor is also known as
    a) Cluster Manager
    b) Virtual Machine Handler
    c) Virtual Machine Manager
    ✅ d) Hypervisor
    *(Correct Option: D)*

10) Which of the following is/are XML parser API(s)?
    a) XaaS (Anything as a Model)
    ✅ b) SAX (Simple API to XML)
    c) CLI (Command Line Interface)
    ✅ d) DOM (Document Object Model)
    *(Correct Option: B, D)*

---

### Assignment-Week 3 (Official Solutions)

*(Not provided in the input data)*

---

### Assignment-Week 4 (Official Solutions)

*(Not provided in the input data)*

---

### Assignment-Week 5 (Official Solutions)

1)  In a SLA negotiation, the provider agreed with the service availability of 98%. The consumer runs the application for X hours/day. At the end of one month [31 days], the total service outage was 12 hrs. However, SLA negotiation (in terms of service availability) is honored.
    ✅ a. X is atleast 19.74
    b. X is atmost 19.74
    c. X is exactly 19.74
    d. Insufficient information
    *(Correct Answer: a)*

2)  Average resource demand is 45 units,Baseline (owned) unit cost is 200 units,Time is 10 hours,Peak resource demand is 100 units. If the cloud is cheaper than owning of computer infrastructures, the utility premium is
    a. Greater than 2.22
    ✅ b. Less than 2.22
    c. Atleast 4.45
    d. Atmost 4.45
    *(Correct Answer: b)*

3)  In computing, there is a linear relationship between the number of processing cores used and power consumption.
    ✅ a. TRUE
    b. FALSE
    *(Correct Answer: a)*

4)  The ______ takes a series of key/value pairs, processes each, and generates zero or more output.
    ✅ a. map function
    b. partition function
    c. reduce function
    d. None of these
    *(Correct Answer: a)*

5)  In a MapReduce framework the HDFS block size is 64 MB. We have 6 files of size 64KB, 65MB, X MB, Y KB, 67KB and 127MB. 24 blocks are created by Hadoop framework. The size of X and Y are respectively [one or more than one options may be correct, select all correct options]:
    a. 66 and 64
    ✅ b. 64 and 64
    ✅ c. 64 and 66
    d. 128 and 64
    *(Correct Answer: b, c)*

6)  Which among the following is/are logical resource(s)?
    a. Network
    b. Computer
    c. Database
    ✅ d. Execution
    *(Correct Answer: d)*

7)  When load decreases, VM management can be done by
    ✅ a. Live migrate VMs to more utilized nodes
    ✅ b. Shutdown unused nodes
    c. Migrate VMs to less utilized nodes
    d. None of these
    *(Correct Answer: a,b)*

8)  Correspondence between resources required by the users and resources available with the provider is known as
    a. Resource provisioning
    b. Resource adaptation
    ✅ c. Resource mapping
    d. None of these
    *(Correct Answer: c)*

9)  Ability or capacity of that system to adjust the resources dynamically to fulfill the requirements of the user is known as
    a. Resource provisioning
    ✅ b. Resource adaptation
    c. Resource mapping
    d. None of these
    *(Correct Answer: b)*

10) Statement 1: Map operation consists of transforming one set of key-value pairs to another. Statement 2: Each reducer groups the results of the map step using the same key.
    ✅ a. Both statements are true
    b. Both statements are false
    c. Statement 1 is true and Statement 2 is false
    d. Statement 1 is false and Statement 2 is true
    *(Correct Answer: a)*

---

### Assignment-Week 6 (Official Solutions)

1)  Interception is considered as an attack on
    ✅ a) Confidentiality
    b) Availability
    c) Integrity
    d) Authenticity
    *(Correct Answer: a)*

2)  Find the correct statement(s):
    ✅ a) Different types of cloud computing service models provide different levels of security services
    ✅ b) Adapting your on-premises systems to a cloud model requires that you determine what security mechanisms are required and mapping those to controls that exist in your chosen cloud service provider
    ✅ c) Data should be transferred and stored in an encrypted format for security purpose
    d) All are incorrect statements
    *(Correct Answer: a, b, c)*

3)  Which of the following is/are example(s) of passive attack?
    a) Replay
    b) Denial of service
    ✅ c) Traffic analysis
    d) Masquerade
    *(Correct Answer: c)*

4)  Modification is considered as an attack on
    (a) Confidentiality
    (b) Availability
    ✅ (c) Integrity
    (d) Authenticity
    *(Correct Answer: c)*

5)  Spoofing is not an example of
    (a) Deception
    ✅ (b) Disclosure
    (c) Usurpation
    ✅ (d) Disruption
    *(Correct Answer: b, d)*

6)  Consider the following statements: Statement I: Authorization is the identification of legitimate users. Statement II: Integrity is the protection against data alteration/corruption. Identify the correct options:
    a) Statement I is TRUE and statement II is FALSE.
    ✅ b) Statement I is FALSE and statement II is TRUE.
    c) Both statements are TRUE.
    d) Both statements are FALSE.
    *(Correct Option: b)*

7)  Access policy control refers to
    ✅ a) Cyclic Inheritance Control
    b) Virus Attack
    ✅ c) Violation of SoD (separation of duties) Constraint
    d) Man in the middle attack
    *(Correct Answer: a, c)*

8)  Which of the options is/are considered as the basic components of security?
    ✅ a) Confidentiality
    ✅ b) Integrity
    c) Reliability
    d) Efficiency
    *(Correct Answer: a, b)*

9)  Which of the following is/are not a type of passive attack?
    a) Traffic Analysis
    b) Release of message contents
    ✅ c) Denial of service
    ✅ d) Replay
    *(Correct Answer: c, d)*

10) Side channel exploitation has the potential to extract RSA & AES secret keys
    ✅ a) True
    b) False
    *(Correct Answer: a)*

---

### Assignment-Week 7 (Official Solutions)

1)  The key features of mobile cloud computing (MCC) are
    ✅ a) Facilitates the quick development, delivery and management of mobile apps
    b) Uses more device resources because applications are cloud-supported
    ✅ c) Improves reliability with information backed up and stored in the cloud
    d) None of these
    *(Correct Answer: a, c)*

2)  Dynamic runtime offloading involves the issues of
    ✅ a) Runtime application partitioning
    ✅ b) Migration of intensive components
    ✅ c) Continuous synchronization for the entire duration of runtime execution platform
    d) None of these
    *(Correct Answer: a, b, c)*

3)  What is/are true about cloudlet?
    a) Increases the latency in reaching the cloud servers
    ✅ b) Reduces the latency in reaching the cloud servers
    c) Resides far from the mobile devices
    ✅ d) Resides near to the mobile devices
    *(Correct Answer: b, d)*

4)  What is/are true about mobile cloud computing (MCC)?
    a) MCC increases the running cost for computation intensive applications
    ✅ b) MCC reduces the running cost for computation intensive applications
    c) MCC decreases battery lifetime
    d) None of these
    *(Correct Answer: b)*

5)  What is/are true about the execution of services in mobile cloud computing (MCC)?
    a) All services are executed in cloud
    ✅ b) Some services are executed in mobile devices and some services are executed in cloud
    c) All computation intensive services are executed in mobile devices
    d) None of these
    *(Correct Answer: b)*

6)  What of the following is/are fog device(s)?
    ✅ a) Cellular base stations
    ✅ b) Network routers
    ✅ c) WiFi Gateways
    d) None of these
    *(Correct Answer: a, b, c)*

7)  What is/are the advantage(s) of fog computing?
    ✅ a) Reduction in data movement across the network resulting in reduced congestion
    b) Increase in data movement across the network resulting in increased congestion
    ✅ c) Serving the real-time applications
    d) None of these
    *(Correct Answer: a, c)*

8)  Consider the following statements: Statement 1: In Geospatial Cloud, it is needed to integrate data from heterogeneous back-end data service. Statement 2: Data services can be inside and/or outside of the cloud environment in Geospatial Cloud.
    a) Statement 1 is Correct, but Statement 2 is Incorrect.
    b) Statement 2 is Correct, but Statement 1 is Incorrect.
    ✅ c) Both statements are Correct.
    d) Both statements are Incorrect
    *(Correct Answer: c)*

9)  Which of the following statement(s) is/are FALSE about Fog Computing?
    a) Fog nodes present near to the end-user
    b) Fog computing enables real-time applications
    ✅ c) Fog nodes' response time is much higher than Cloud's
    ✅ d) Network routers, WiFi Gateways will not be capable of running applications
    *(Correct Answer: c, d)*

10) Which of the following is/are true about Geospatial Cloud Model?
    a) It integrates data from homogeneous back-end data services
    ✅ b) Data services can be inside and/or outside the cloud environment
    c) Data services inside cloud can be run through SaaS service model
    d) None of the above
    *(Correct Answer: b)*

---

### Assignment-Week 8 (Official Solutions)

1)  An IoT platform's basic building blocks is/ are (choose the correct option(s)).
    ✅ a. Gateway
    b. Images
    ✅ c. Network and Cloud
    d. Containers
    *(Correct Answer: a, c)*

2)  ______ is used to delete a local image.
    a. Docker rm
    ✅ b. Docker rmi
    c. Docker rvi
    d. Docker push
    *(Correct Answer: b)*

3)  Docker Hub is a registry used to host various docker images.
    ✅ a) True
    b) False
    *(Correct Answer: (a))*

4)  ______ enables different networks, spreads in a huge geographical area to connect together and be employed simultaneously by multiple users on demand.
    a) Serverless
    b) IoT Cloud
    ✅ c) Sensor Cloud
    d) Green Cloud
    *(Correct Answer: c)*

5)  Virtual machines get virtual access to host resources through a ______
    a) Containers
    ✅ b) Hypervisor
    c) Both a and b
    d) Images
    *(Correct Answer: b)*

6)  Vehicles providing their networking and data processing capabilities to other vehicles through the cloud comes under which service of IoT-based Vehicular Data Clouds.
    a) SaaS
    b) PaaS
    ✅ c) IaaS
    d) None of these
    *(Correct Answer: c)*

7)  Sensor data can be easily shared by different groups of users without any extra effort/ measure.
    a. True
    ✅ b. False
    *(Correct Answer: b)*

8)  Container is a compile time instance of an image.
    a) True
    ✅ b) False
    *(Correct Answer: (b))*

9)  In the context of Green Cloud Computing, the Power Usage Effectiveness is defined as
    a. Power Delivered / Overall Power
    ✅ b. Overall Power / Power Delivered
    c. Overall Power * Power Delivered
    d. None of these
    *(Correct Answer: b)*

10) Statement 1: Sensor-Cloud proxy exposes sensor resources as cloud services. Statement 2: Sensor network is still managed from the Sensor-Cloud Interface via Sensor Network Proxy
    a. Statement 1 is True and Statement 2 is False
    b. Statement 2 is True and Statement 1 is False
    ✅ c. Both statements are True
    d. Both statements are False
    *(Correct Answer: c)*

---

### Assignment-Week 9 (Official Solutions)

1)  Which of the following statements best describes fog computing?
    a) Fog computing refers to a model where data, processing, and applications are concentrated in the cloud rather than at the network edge.
    b) Fog computing is a term introduced by Cisco Systems to describe a model that centralizes data processing in the cloud to manage wireless data transfer to distributed IoT devices.
    ✅ c) Fog computing is a model where data, processing, and applications are concentrated in devices at the network edge rather than existing almost entirely in the cloud.
    d) The vision of fog computing is to enable applications on a few connected devices to run directly in the cloud without interaction at the network edge.
    *(Correct Answer: (c))*

2)  Which of the following challenges is most effectively addressed by using fog and edge computing instead of a "cloud-only" approach for IoT applications?
    a) Resource management issues related to workload balance and task scheduling in cloud-based environments.
    ✅ b) The inefficiency of processing time-sensitive applications directly in the cloud due to high latency and large data bandwidth requirements.
    c) The need for improved security and privacy features in cloud-based systems, which are not addressed by fog and edge computing.
    d) The difficulty in integrating multiple cloud services and platforms for comprehensive IoT data management.
    *(Correct Answer: (b))*

3)  Which of the following correctly describes a classification of resource management architectures in fog/edge computing? Threads of a process share *(Note: Question text seems unrelated to options provided in source)*
    a) Data Flow
    b) Control.
    ✅ c) Tenancy.
    d) Infrastructure.
    *(Correct Answer: (c))*

4)  Which of the following characteristics is NOT typically associated with fog computing infrastructure?
    a) Location awareness and low latency
    b) Better bandwidth utilization
    ✅ c) High computational power concentrated solely in the Cloud
    d) Support for mobility
    *(Correct Answer: (c))*

5)  In the fog computing paradigm, which of the following accurately describes the relationship between local and global analyses?
    a) Local analyses are performed exclusively in the Cloud, while global analyses are done at the edge devices.
    b) Local and global analyses are performed only in the Cloud data centers.
    ✅ c) Local analyses are performed at the edge devices, and global analyses can be either performed at the edge or forwarded to the Cloud.
    d) Local analyses are conducted by IoT devices, and global analyses are not necessary in fog computing.
    *(Correct Answer: (c))*

6)  What is the primary goal of the application placement problem in the Cloud-Fog-Edge framework?
    a) To map all applications onto the Cloud servers to maximize computational power.
    ✅ b) To find available resources in the network that satisfy application requirements, respect constraints, and optimize the objective, such as minimizing energy consumption.
    c) To place all application components on edge devices to ensure low latency.
    d) To disregard resource capacities and focus solely on network constraints.
    *(Correct Answer: (b))*

7)  Which of the following is an example of an application constraint in the application placement problem on the Cloud-Fog-Edge framework?
    a) Finite capabilities of CPU and RAM on infrastructure nodes.
    b) Network latency and bandwidth limitations.
    ✅ c) Locality requirements restricting certain services' executions to specific locations.
    d) Availability of storage resources in the Fog nodes.
    *(Correct Answer: (c))*

8)  What is the primary purpose of offloading in the context of edge computing?
    a) To move all data processing from edge nodes to the cloud.
    ✅ b) To augment computing requirements by moving servers, applications, and associated data closer to the network edge.
    c) To reduce the number of user devices connected to the network.
    d) To centralize all computational resources in the cloud for better performance.
    *(Correct Answer: (b))*

9)  What is the primary goal of a cloud federation?
    a) To centralize all cloud services under a single provider.
    ✅ b) To deploy and manage multiple cloud services to meet business needs by collaborating among different Cloud Service Providers (CSPs).
    c) To limit the geographical reach of cloud services.
    d) To reduce the number of cloud service providers globally.
    *(Correct Answer: (b))*

10) Which of the following is a key benefit of forming a cloud federation?
    a) Centralized control of global cloud services.
    ✅ b) Increased resource utilization and load balancing across multiple Cloud Service Providers (CSPs).
    c) Reduced collaboration among Cloud Service Providers.
    d) Limiting the geographical footprint of Cloud Service Providers.
    *(Correct Answer: (b))*

---

### Assignment-Week 10 (Official Solutions)

1)  Post-copy and Pre-copy migration approaches are employed in :
    ✅ a. Live Migration process
    b. Non-live Migration process
    c. Hybrid Migration process
    d. None of these
    *(Correct Answer: a)*

2)  Kubernetes operates at the hardware level.
    a. True
    ✅ b. False
    *(Correct Answer: b)*

3)  What is(are) the key advantage(s) of Docker?
    ✅ a. Facilitating microservices
    ✅ b. Modeling networks.
    ✅ c. Packaging software
    d. None of these
    *(Correct Answer: a,b,c)*

4)  Which of the following statements is most appropriate about Docker ?
    a. Docker is a platform that allows to build and run but not ship apps.
    b. Docker is a platform that allows to build and ship but but not to run apps.
    ✅ c. Docker is a platform that allows to build, ship and, run apps.
    d. Docker is a platform that only allows to ship and run but not to build apps.
    *(Correct Answer: c)*

5)  In Docker utility, ______ is a collection of filesystem layers and some metadata that, if taken together, can be spun up as Docker containers.
    a. Operating System
    b. Microservice
    c. Virtual Machine
    ✅ d. Image
    *(Correct Answer: d)*

6)  Containers are similar to VMs but they have unrelaxed isolation properties to share the operating system among the applications.
    a. True
    ✅ b. False
    *(Correct Answer: b)*

7)  Choose the most appropriate option. Statement 1: Container is a lightweight virtualization technique. Statement 2: Container contains the code and all its dependencies.
    a. Only statement 1 is true
    b. Only statement 2 is true
    ✅ c. Both statement 1 and 2 are true
    d. Bothe the statements are false
    *(Correct Answer: c)*

8)  Private Docker registry is a service that stores Docker images.
    ✅ a. True
    b. False
    *(Correct Answer: a)*

9)  Docker builds offer enhanced reproducibility and replicability compared to conventional software development approaches.
    ✅ a. True
    b. False
    *(Correct Answer: a)*

10) Given the VM memory size of 1024 GB and the transmission rate of 16 MB/sec What are the total migration time and downtime for non-live VM migration? Choose the most appropriate option.
    a. 20 hours, 25 hours
    ✅ b. 18 hours, 18 hours
    c. 16 hours, 16 hours
    d. 24 hours, 20 hours
    *(Correct Answer: b)*

---

### Assignment-Week 11 (Official Solutions)

*(Note: Question text was missing from source images for this week's official solutions. Answers are included based on the provided correct options.)*

1)  (Question text missing)
    ✅ (a)
    *(Correct Answer: (a))*

2)  (Question text missing)
    ✅ (d)
    *(Correct Answer: (d))*

3)  (Question text missing)
    ✅ (b)
    *(Correct Answer: (b))*

4)  (Question text missing)
    ✅ (b)
    *(Correct Answer: (b))*

5)  (Question text missing)
    ✅ (b)
    *(Correct Answer: (b))*

6)  (Question text missing)
    ✅ (b)
    *(Correct Answer: (b))*

7)  (Question text missing)
    ✅ (a), (b), and (c)
    *(Correct Answer: (a), (b), and (c))*

8)  (Question text missing)
    ✅ (c)
    *(Correct Answer: (c))*

9)  (Question text missing)
    ✅ (a)
    *(Correct Answer: (a))*

10) (Question text missing)
    ✅ (b)
    *(Correct Answer: (b))*

---

### Assignment-Week 12 (Official Solutions)

1)  In which computing environment is latency fixed due to the location of application modules at the Area Gateway?
    ✅ A) Fog computing
    B) Cloud computing
    C) Serverless Computing
    D) None of the above
    *(Correct Answer: A)*

2)  What does spatial cloud support in terms of resource pooling?
    A) Individual resource allocation for participating organizations
    B) Exclusive resource ownership for each organization
    ✅ C) Shared resource pooling for participating organizations
    D) Restricted access to network, servers, apps, services, storages, and databases
    *(Correct Answer: C)*

3)  Dew computing is an on premises computer software-hardware organization paradigm where on-premises computers provide functionality that is ______ of cloud services and is also ______ with cloud services.
    A) independent, serverless
    B) dependant, collaborative
    ✅ C) independent, collaborative
    D) serverless, collaborative
    *(Correct Answer: C)*

4)  Fog-Edge computing leads to increased network congestion
    A) True
    ✅ B) False
    *(Correct Answer: B)*

5)  A Cyber-Physical Cloud Computing (CPCC) architectural framework is a ______ environment that can rapidly build, modify and provision cyber-physical systems composed of a set of ______ based sensor, processing, control, and data services.
    ✅ A) system, cloud computing
    B) cloud computing, system
    C) system, edge computing
    D) edge, system computing
    *(Correct Answer: A)*

6)  What is(are) the key feature(s) of Mobile Cloud computing for 5G networks?
    A) Increased resource consumption by mobile applications
    ✅ B) Improved reliability due to data storage in the cloud
    ✅ C) Sharing resources for mobile applications
    D) None of these
    *(Correct Answer: B and C)*

7)  The key aspect of the intelligent transportation system is efficient ______
    A) cost
    ✅ B) mobility
    C) speed
    D) delivery
    *(Correct Answer: B)*

8)  In conjunction with 5G and cloud computing, what should service providers focus on in the evolving computing paradigm?
    A) Limiting end-to-end orchestration
    B) Providing manual service layer agreements
    C) Offering limited self-service options
    ✅ D) Providing full end-to-end orchestration with defined service layer agreements
    *(Correct Answer: D)*

9)  Mobility Analytics utilizes the cloud platform for computation and storage.
    ✅ A) True
    B) False
    *(Correct Answer: A)*

10) What is(are) the benefit(s) of 5G technology for enhanced mobile broadband?
    A) Slower data rates
    B) Higher latency
    ✅ C) Lower cost-per-bit
    D) Limited device compatibility
    *(Correct Answer: C)*

---

""" # --- Text ka end ---

# --- PDF Configuration ---
pdf_filename = "NPTEL_Cloud_Computing_QA_Formatted.pdf"
font_path_regular = 'DejaVuSans.ttf'
font_path_bold = 'DejaVuSans-Bold.ttf'
font_path_italic = 'DejaVuSans-Oblique.ttf' # Oblique often used for Italic style

font_name = 'DejaVu'

# --- PDF Generation Logic ---
class PDF(FPDF):
    def header(self):
        pass # No header

    def footer(self):
        # Page number footer
        self.set_y(-15)
        try:
            # Use DejaVu if loaded, else fallback
            current_font = self.font_family
            if font_name.lower() != current_font.lower():
                 self.set_font(font_name, 'I', 8)
        except:
            self.set_font('Arial', 'I', 8) # Fallback
        page_num = self.page_no()
        self.cell(0, 10, f'Page {page_num}', 0, 0, 'C')

# Check if ALL font files exist
font_files = [font_path_regular, font_path_bold, font_path_italic]
fonts_missing = False
for f_path in font_files:
    if not os.path.exists(f_path):
        print(f"ERROR: Font file '{f_path}' nahi mila.")
        fonts_missing = True

if fonts_missing:
    print("Kripya zaroori DejaVu font files (.ttf) download karke script wale folder mein rakhein.")
    print("Script ab band ho rahi hai.")
    sys.exit(1)

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=20) # 2cm bottom margin

# Add and set the fonts
font_loaded = False
try:
    pdf.add_font(font_name, '', font_path_regular)
    pdf.add_font(font_name, 'B', font_path_bold)
    pdf.add_font(font_name, 'I', font_path_italic)
    pdf.set_font(font_name, '', 10) # Default font
    print(f"Font '{font_name}' (Regular, Bold, Italic) successfully load ho gaya.")
    font_loaded = True
except Exception as e:
     print(f"Font add karne mein Error: {e}")
     print("Arial font istemal hoga (checkmarks/bolding theek se nahi dikhega).")
     pdf.set_font("Arial", size=10)
     font_loaded = False

# Function to set font safely
def set_font_safe(style='', size=10):
    font_to_use = font_name if font_loaded else 'Arial'
    final_style = style.upper()
    # Ensure combination exists, otherwise fallback to regular for that font
    # (fpdf2 doesn't raise error here, just uses available style)
    pdf.set_font(font_to_use, final_style, size)


# --- PROCESS LINES ---
lines = copied_text.strip().split('\n')
is_first_question = True # Flag to handle spacing before first question

# Regex to identify question lines (number followed by ')')
question_pattern = re.compile(r"^\s*(\d+)\)\s")

for line in lines:
    # Replace emoji BEFORE stripping whitespace to catch indented emojis
    line = line.replace('✅', '✓') # Replace emoji with text checkmark
    line_stripped = line.strip()

    if not line_stripped:
        # Don't add extra space for consecutive blank lines
        # pdf.ln(2)
        continue

    is_question_line = question_pattern.match(line_stripped)

    # Add spacing before a new question (except the first one)
    if is_question_line and not is_first_question:
        pdf.ln(5) # Add extra vertical space
    if is_question_line:
        is_first_question = False # Mark that first question is processed

    # --- Styling Logic ---
    if line.startswith('### '):
        set_font_safe('B', 11)
        pdf.multi_cell(0, 5.5, line[4:].strip(), ln=1, align='L')
        pdf.ln(1)
    elif line.startswith('## '):
        set_font_safe('B', 13)
        pdf.multi_cell(0, 6.5, line[3:].strip(), ln=1, align='L')
        pdf.ln(2)
    elif line.startswith('# '):
        set_font_safe('B', 15)
        pdf.multi_cell(0, 7.5, line[2:].strip(), ln=1, align='C')
        pdf.ln(3)
    elif line_stripped == '---':
        pdf.ln(2)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(4)
    elif line_stripped.startswith('*(Correct'):
        set_font_safe('I', 9)
        pdf.multi_cell(0, 4.5, line_stripped, ln=1, align='L')
        pdf.ln(0.5)
    elif line_stripped.startswith('✓ '): # Correct Option - BOLD
        set_font_safe('B', 10) # Set BOLD
        pdf.set_x(pdf.l_margin + 5)
        cell_width = pdf.w - pdf.l_margin - pdf.r_margin - 5
        pdf.multi_cell(cell_width, 5, line_stripped, ln=1, align='L')
        pdf.ln(0.1)
    elif is_question_line: # Question Line - BOLD
        set_font_safe('B', 10) # Set BOLD
        pdf.multi_cell(0, 5, line_stripped, ln=1, align='L')
        pdf.ln(0.5)
    elif line_stripped.startswith(('a)', 'b)', 'c)', 'd)', 'A)', 'B)', 'C)', 'D)')): # Incorrect options - Regular
        set_font_safe('', 10) # Set Regular
        pdf.set_x(pdf.l_margin + 5)
        cell_width = pdf.w - pdf.l_margin - pdf.r_margin - 5
        pdf.multi_cell(cell_width, 5, line_stripped, ln=1, align='L')
        pdf.ln(0.1)
    elif line_stripped: # Other Regular text (like statements within questions)
        set_font_safe('', 10) # Set Regular
        pdf.multi_cell(0, 5, line_stripped, ln=1, align='L')
        pdf.ln(0.5)

    # Reset font to default regular after processing each line
    # This ensures the next line starts with the default unless specifically styled
    set_font_safe('', 10)


# --- Save PDF ---
try:
    pdf.output(pdf_filename)
    print(f"PDF '{pdf_filename}' safaltapoorvak ban gayi!")
except Exception as e:
    print(f"PDF save karne mein Error: {e}")