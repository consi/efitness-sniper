eFitness.com.pl booking sniper
==============================

This small utility books trainings on eFitness.com.pl in your name. Be always first on list for your favourite training. Code basically allows my wife to always attend her favourite trainings :)

Installation
============
```
pip install efitness-sniper
```

Usage
=====
Create file `.efitness.yml` in your home directory with:

```
---
login_data:
  subdomain: modelarnia-bb-cms # this is a subdomain of club (example for http://modelarnia-bb-cms.efitness.com.pl)
  user: your_login_name # specify your account login
  password: your_password # specify account password

sniper_rules: # You can define as much rules as you want :)
# How much days script should look forward (if bigger - it traverses more calendar pages, so I recommend to set it n+1 day
# where n is maximum time before allowed registration) - minimum here is 3 (due to cancellation policy)
# lower values will be overriden to 3
  - look_ahead_days: 6 
    match: "BODY BALL" # Name of training - you can use part of name, eg. BALL will match BODY BALL
    day_of_week: 0 # Specify day of week that you are interrested in (0 - Monday)
    after_hour: 16:00 # Do not book trainings before 4PM
    before_hour: 21:00 # Do not book trainings after 9PM
  - look_ahead_days: 6 # Another training definition
    match: "TRX"
    day_of_week: 2
    after_hour: 18:00
    before_hour: 21:00
```

Add `efitness` command to your crontab - I recommend to not do it more often than 15min, so: `*/15 * * * *`

License
=======

```
MIT License
Copyright (c) 2020 Marek Wajdzik
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
