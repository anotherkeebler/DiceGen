# Diceware password generator server


    docker run --detach --rm --name hello-sinatra -p 8180:80 -v $PWD:/usr/src/app -e MAIN_APP_FILE=hello.rb -e RACK_ENV=development erikap/ruby-sinatra
