# 0x0C. Web server
## Resources
- [How the web works](developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](en.wikipedia.org/wiki/Nginx)
- [How to configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Child process concept page](intranet.alxswe.com/concepts/110)
- [Root and sub domain](landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](tutorialspoint.com/http/http_methods.htm)
- [HTTP redirection](moz.com/learn/seo/redirection)
- [Not found HTTP response code](en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
- man or help scp
- man or help curl

## Learning Objectives
### General
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests
### DNS
- What DNS stands for
- What is DNS main role
### DNS Record Types
- A
- CNAME
- TXT
- MX

## Tasks
### Task 0
- File: 0-transfer_file
transfers a file from our client to a server
### Task 1
- File: 1-install_nginx_web_server
Install nginx on web-01
### Task 2
- File: 2-setup_a_domain_name
Setup a domain name by following these steps:
 Access the tools space
 Unlock the GitHub student pack: WARNING - this invitation link is unique to you and can’t be reclaimed! If you have any issue, please contact GitHub education support
### Task 3
- File: 3-redirection
Configure the Nginx server so that /redirect_me is redirecting to another page.
### Task 4
- File: 4-not_found_page_404
Configure the Nginx server to have a custom 404 page that contains the string "Ceci n'est pas une page."
