Feature: Monster tr sitesi login

Scenario: Monster TR sitesi mail ve şifre ile başarılı login
  Given I launch chrome browser
  When I open monster tr login page
  And Accept Onetrust
  And Enter mail "Username or mail" and password "password"
  And Click login button
  Then User must successfully login to website
  And Close browser
