cd news_rider
go get github.com/ericchiang/pup
pip3.6 install -r requirements.txt --user
bash ./scripts/start_screen.sh news_rider_bot 'GOOGLE_APPLICATION_CREDENTIALS=$HOME/service-account.json python3.6 main.py -c commands.txt'