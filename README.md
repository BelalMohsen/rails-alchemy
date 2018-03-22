# rails-alchemy
RailsAlchemy transforms development raw text requirements into an up and running Rails application.<br>
Example<br>
$ python statAlchemy.py -r 'Every student belongs to a school. A school is managed by a director. Every director manages one or more teachers.' -d /tmp -e 'yes'<br>
 ____       _ _        _    _      _<br>                           
|  _ \ __ _(_) |___   / \  | | ___| |__   ___ _ __ ___  _   _<br>
| |_) / _` | | / __| / _ \ | |/ __| '_ \ / _ \ '_ ` _ \| | | |<br> 
|  _ < (_| | | \__ \/ ___ \| | (__| | | |  __/ | | | | | |_| |<br> 
|_| \_\__,_|_|_|___/_/   \_\_|\___|_| |_|\___|_| |_| |_|\__, |<br> 
                                                        |___/<br>  

You app description<br> 
Every student belongs to a school. A school is managed by a director. Every director manages one or more teachers.<br>

The Alchimist is analyzing your requirements..<br> 
-> Installing Gems<br> 
-> Installing devise<br> 
-> Creating devise user..<br> 
-> Creating devise views..<br> 
-> Creating a scaffold for school<br> 
-> Adding before action to application controller<br> 
-> Adding role options to signup<br> 
-> Migrating the database<br> 
-> Launching rails server<br> 
