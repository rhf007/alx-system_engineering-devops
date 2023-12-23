# MySQL

![mysql](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png)

## What is the main role of a database

* **Data Storage:**

    Databases are designed to store large amounts of data in a structured format.
    They use tables to organize data into rows and columns, allowing for efficient storage and retrieval.

* **Data Retrieval:**

    Databases provide mechanisms for querying and retrieving specific data based on various criteria.
    Users can use SQL (Structured Query Language) or other query languages to interact with the database and extract information.

* **Data Integrity:**

    Databases enforce data integrity rules to ensure that the stored data is accurate and consistent.
    Integrity constraints, such as primary keys and foreign keys, help maintain the quality of the data.

* **Concurrency Control:**

    Databases manage concurrent access to data by multiple users or applications.
    Mechanisms like transactions and locking ensure that multiple operations can be performed simultaneously without compromising data consistency.

* **Data Security:**

    Databases implement security measures to control access to sensitive data.
    Authentication, authorization, and encryption are commonly used to protect databases from unauthorized access.

* **Data Relationships:**

    Databases support the establishment of relationships between different sets of data.
    Relationships, such as one-to-one, one-to-many, or many-to-many, help model complex data structures.

* **Scalability:**

    Databases are designed to scale with the growing volume of data and increasing user demands.
    Scalability can be achieved through techniques like replication, sharding, and clustering.

* **Data Backup and Recovery:**

    Databases include mechanisms for regular data backup to prevent data loss in the event of hardware failures or other disasters.
    Recovery features help restore the database to a consistent state after a failure.

* **Performance Optimization:**

    Databases optimize query execution and data retrieval through indexing, caching, and query optimization techniques.
    Performance tuning is a critical aspect of maintaining a responsive and efficient database system.

## What is a database replica

The process of creating copies of a database and storing them across various  destinations. It improves data availability and accessibility. Every user connected to the system can access copies of the same (up-to-date) data.

If your important data is stored in an SQL database (MySQL, MariaDB, PostgreSQL, etc.), you can take advantage of some built-in replication features. These can be used to provide a failover system in case the main server goes down.

### Master-Slave Replication

The most basic kind of SQL replication is a Master-Slave configuration. In this scenario, you have a main database server, which is referred to as the “master” server. This server is responsible for performing all writes and updates. The data from this server is copied continuously to a “slave” server. This server can be be read from, but not written to.

This setup allows you to distribute the reads across multiple machines, which can dramatically improve your application’s performance.

While this performance increase is an advantage, one of the main reasons you may set up master-slave replication is for handling failover. If your master server becomes unavailable, you can still read from your slave server. Furthermore, it is possible to convert the slave into a master server in the event that your master is offline for an extended period of time.

Master-slave replication is, in fact, one area where we begin to see how redundancy and backups can complement each other. In a master-slave configuration, you can replicate data from the master to the slave. You can then temporarily disable replication to maintain a consistent state of information on the slave. From here, you can back up the database using whatever backup mechanism is appropriate.

### Master-Master Replication

A second form of replication is called Master-Master replication. This configuration allows both servers to have “master” abilities. This means that each server can accept writes and updates and will transfer the changes to the opposite server. This configuration inherits the advantages of the master-slave setup, but also benefits from increased write performance if the writes are properly distributed by a load balancing mechanism.

This also means that, in the event that one server goes down, the other is still up and ready to accept requests. While the configuration is more complicated, the failover in the event of a problem is less complicated than the master-slave redundancy, because the slave database does not need to transform into the master.

This configuration can also be combined with a backup mechanism if you take one of the master servers offline. You must maintain a static database for backups to function correctly, so you have to ensure that no data is being modified or written to until after the backup is complete.

## What is the purpose of a database replica

Well, of course the most common answers are accessibility, reliability and all of that. It's pretty obvious really.

When a database becomes corrupted for some reason you need to be able to restore the data to the last know point in time when the database was in a consistent state.  In order to do this you need to make sure you have backup strategy that supports a variety of different restore situations.  Therefore developing a backup procedure that makes sure you can do restores should be one of your top priorities as a DBA.

One never knows what might happen to a database.  It might get corrupted due to some bad code, or bad hardware.  It might even get lost due to a data center fire, flooding, or some other catastrophic event.  In order to recover from data corruption or total loss of a database you need to back up your databases based on some requirements.

## Why database backups need to be stored in different physical locations

For all sorts of reasons you can imagine, honestly. Backup requirements are important, but you also need to think about where you place your database backups.  You need to have your backup files readily available if should you need them.  But you need to make sure they are not vulnerable to a server melt down, or a total data center disaster.  Therefore you need to consider where to store your backup files onsite, as well as where you might store your backup files offsite.

For onsite backups you need to write or store your backup files so they are available in the event your database server should crash, or a database gets corrupted.   Placing your backups directly on your database server allows you to write your backups fast because there is no network I/O that has to occur.  But if your backups are on your database server, and the server should melt down then you have lost your backups.  An alternative to this is to write your backups to a network drive.  This keeps your backups off your database server, but does not provide for a secondary location should the machine where your network backups are stored have a problem.  It is always best to make sure your backups are copied to a secondary backup location, like tape, or a network backup storage solution.   This way should the primary backup device not be available, than you can always get your backups from the secondary location.   You should make sure your backups are copied to the secondary location soon after they are created.  This minimizes the time that you only have a single backup copy.

Having your backup’s onsite allows you to quickly obtain a backup file should you need to do a restore.  But what happens when your onsite facility has a problem like a major fire, flood, or is damage by some other natural disaster?  If something happens to your onsite backups, then you will not be able to recover unless you have taken the precautions of copying your backups to an offsite location.  As you are developing your backup solution you need to develop a plan that copies your backup files to a secure offsite storage location.

## What operation should you regularly perform to make sure that your database backup strategy actually works

Just because you have backed up your databases doesn’t mean you can restore your databases from a backup.  After you have created your backups you should probably verify that the backups are good.  There are a couple of options to accomplish this. 

One of those options is to occasionally perform an actual restore of your databases from those backups you have taken.  This might not be practical in your production environment, but you should at least periodically test to make sure you can restore your backups in some non-production environment. 

Additionally you can verify the backups are written correctly.  This can be accomplished with the “BACKUP VERIFYONLY” command.  This command actually reads the backup file and verifies that the data in the backup can actually be restored.  By using the verify option SQL Server will be able to detect if the backups were writing correctly.

Restoring a single database backup only means you can restore that single backup, but not a complete set of backups.  You should consider periodically doing a complete bare metal restore.  This is where you would find an unused machine and try to restore the OS, SQL Server software, and all the databases including the system databases.  Performing a complete server restore will give you the confidence in your backup strategy and will reduce your anxiety when you have a real disaster where you have to do a complete restore.
