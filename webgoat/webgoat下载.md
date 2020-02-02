* 解决的几个问题

  1. 宿主机上无法用ping命令

     增加PATH：“c://Windows/Systems”

  2. vb上虚拟机apt无法下载

     换源`sudo  apt update`

  3. 主机ping不通vb上的虚拟机

     * 关闭虚拟的防火墙`sudo ufw disable  关闭` `sudo ufw enable 开启`
     * 增加桥接网络网卡可以ping通

  4. 远程宿主机ssh登录虚拟机,ssh连接不成功的原因

      - 虚拟机要下载 `openssh-server `

      - 检查ssh服务是否开启

        ```
        sudo service ssh status    
        sudo service ssh start
        ```

     * `iptables`在该系统中检查端口22是否被阻塞。只需允许端口进入`iptables`，然后检查即可。 

       ```bash
       sudo iptables -A INPUT -p tcp --dport ssh -j ACCEPT
       ```

     *  否则`ssh`，通过编辑将端口号从22 更改为2222 

       ```bash
       vi etc/ssh/sshd_config    
       /etc/init.d/ssh restart.
       ```

5. 复制虚拟机到其他vritualbox上后NAT网卡不能用

   解决办法，virtualbox全局设置->网络->添加NAT网络

* 安装docker

  ```bash
  安装依赖包：# sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y  
  添加官方密钥，执行此命令可能需要代理，显示Ok表示执行成功：# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
  添加仓库：# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable"  
  更新apt镜像源：# sudo apt update 
  执行此行命令安装docker-ce:# sudo apt install docker-ce -y 
  查看安装的版本：# docker --version 
  ```

* 安装docker-compose

  ```bash
  下载docker-compose 1.24.1:# sudo curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose 
   查看docker-compose版本：# chmod +x /usr/local/bin/docker-compose  
  查看版本:# docker-compose --version 
  ```

* 配置加速器

  ```bash
  # curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
  ```

  * 虚拟机备份

* webgoat容器下载

  ```bash
  docker run -d -p 8080:8080 -p 9090:9090 -e TZ=Europe/Amsterdam webgoat/goatandwolf
  ```

* 

