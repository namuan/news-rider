# News Rider

A python application to fetch interested feeds from different sources and generates a markdown file (or send tweets).

### Requirements

* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installation-guide) / [Ansible Galaxy](https://galaxy.ansible.com)
* Python 3.5+
* [DigitalOcean account](https://m.do.co/c/da51ec30754c)
* [doctl](https://github.com/digitalocean/doctl) To manage DigitalOcean droplets
* [OpenSSH 7.3](http://man.openbsd.org/ssh_config) (That version features an Include directive for ssh_config(5)).

  This is required so that we can include the generated config file after building the VM

  ```
  $ cat ~/.ssh/config
    Include config.d/config-*
  ```

##### Variables

* DIGITALOCEAN_ACCESS_TOKEN (Used when provisioning DigitalOcean droplet)

Copy .env.sample to .env and populate with twitter credentials (only if twitter mode is enabled)

* CONSUMER_KEY
* CONSUMER_SECRET
* ACCESS_TOKEN_KEY
* ACCESS_TOKEN_SECRET

##### Setting up News sources

The application expects a list of commands in commands.txt file which should generate a list of links. 
You can use any tools to scrape the news source for interesting sources. In the commands.txt.sample, I'm using
`curl` alongside `pup` to extract the HTML elements containing links. 

Copy commands.txt.sample to commands.txt and provide a command on each link which generates a list of links.  

## Installation

```
pip3 install -r requirements.txt
```

## Usage

* All the commands supported by the Makefile

```
$ make

 Choose a command run in news_rider:

  backup       Copies the database from server to data/ directory
  restore      Copies the local database to server
  clean        Cleans all cached files
  deploy       Copies any changed file to the server
  start        Sets up a screen session on the server and start the app
  show-vms     Shows all the VMs running on DigitalOcean
  destroy-vm   Destroys the VM on DigitalOcean running for the project
  ssh          SSH into the target VM
  infra        Sets up a virtual machine on DigitalOcean and updates the local SSH configuration
```

For now, running the Ansible scripts require Python 2.7

Setup a Droplet. Grab a quick cup of ☕️ while this is running

```
make infra
```

Once the droplet is provisioned, the Makefile will create SSH configuration file in ~/.ssh/config.d folder

If you are using the SSH config Include directive then you can SSH into the running VM

```
make ssh
```

To list all the running VMs

```
# requires doctl
make show-vms
```

To deploy the python application

```
make deploy
```

To start the python application.
This will run the app in a screen session

Restore it on the server before starting the app

```
make restore # run only if database restore is required
make start
```

After running you can SSH and connect with the running Screen session

```
make ssh
screen -x
```

## Docker support

To run it with Docker, first build the image using the provided `Dockerfile`

```
docker build -t namuan/news_rider .
```

Once built, it can be run with providing the `.env` file and sharing the local database so that it can be synced

```
docker run -v ${PWD}/data/news_rider.db:/root/news_rider.db:rw --env-file=.env -it namuan/news_rider
```

## Setting it up on RaspberryPi

Setup an entry in ssh config with the same project name but pointing to RaspberryPi IP address

```
Host news_rider
	User pi
	HostName 192.168.1.77
	Port XXXX
	IdentitiesOnly yes
	IdentityFile ~/.ssh/id_xxx
```

Then we need to upgrade to Python3.6. This just means following the instructions listed [here](https://gist.github.com/SeppPenner/46349b29d90f71fe14319c59f2d7e4e4)

Once we have Python3.6 setup, the above Makefile commands should work with setting it up on Raspberry Pi.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
