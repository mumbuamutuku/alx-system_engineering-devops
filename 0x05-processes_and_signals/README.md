0x05. Processes and signals

0-what-is-my-pid - Write a Bash script that displays its own PID.

1-list_your_processes - Write a Bash script that displays a list of currently running processes.

2-show_your_bash_pid -sing your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process

3-show_your_bash_pid_made_easy - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

4-to_infinity_and_beyond - Write a Bash script that displays To infinity and beyond indefinitely.

5-dont_stop_me_now  - We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:
You must use kill

6-stop_me_if_you_can - Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:
You cannot use kill or killall

7-highlander - Write a Bash script that displays:
To infinity and beyond indefinitely

With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

8-beheaded_process - Write a Bash script that kills the process 7-highlander.

100-process_and_pid_file - Write a Bash script that:

Creates the file /var/run/myscript.pid containing its PID

Displays To infinity and beyond indefinitely

Displays I hate the kill command when receiving a SIGTERM signal

Displays Y U no love me?! when receiving a SIGINT signal

Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

