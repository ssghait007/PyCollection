
1. **Ensure that crond.service is active and enabled:**

```systemctl status crond.service```

If we see an active (running) status, then everything is good to go.

2. **Verify that /usr/local/bin/loadavg.sh is Executable for All and Produces Correct Output**
Check permissions on /usr/local/bin/loadavg.sh:

```ls -l /usr/local/bin/loadavg.sh```

Make it executable:
```chmod a+x /usr/local/bin/loadavg.sh```
Run the script:

```/usr/local/bin/loadavg.sh```
Check to see if the script sent data to /var/log/loadavg.log:

```cat /var/log/loadavg.log```
We should see a timestamp and the three load averages in there.

3. **Create a cron Job that Executes /usr/local/bin/loadavg.sh Once per Minute During the Hours of 8AM-5PM on Monday through Friday**
Use **crontab -e** to create the following content:
Save the cronjob and check our work:
```crontab -l```

4. **Verify Cronjob is Running and Producing Correct Output**
Again, we could verify **crond.service** is running using **systemctl**. If we want to know whether our job is running or not, we can run **tail/var/log/cron** after a few minutes, and we should see entries in there for our loadavg.sh script. We should also take a look at the log that the script is writing to, with:
```
systemctl status crond.service
tail /var/log/cron
cat /var/log/loadavg.log
```
If the job is running, then we'll see contents like we did when we ran the script manually, once a minute.
