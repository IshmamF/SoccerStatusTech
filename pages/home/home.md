<|text-center|
<br/>
<br/>
<br/>
<br/>
<br/>
<h2>Welcome to the English Premier League Visualization Tool!</h2>
>
<|text-center|
<br/>
<|card|
<h3>Choose your team</h3>
>
<|layout|gap=10px|class_name=container align_center|
<center>
<|{value1}|selector|lov=Arsenal;Aston Villa;Bournemouth;Brentford;Burnley;Wolverhampton;Brighton Hove; Chelsea;Crystal Palace;Everton;Fulham;Liverpool;Luton Town;Man City;Man United;Newcastle;Nottingham;Sheffield Utd;Tottenham;West Ham|dropdown|label=Team 1|>
</center>

<center>
<|{value2}|selector|lov=Arsenal;Aston Villa;Bournemouth;Brentford;Burnley;Wolverhampton;Brighton Hove; Chelsea;Crystal Palace;Everton;Fulham;Liverpool;Luton Town;Man City;Man United;Newcastle;Nottingham;Sheffield Utd;Tottenham;West Ham|dropdown|label=Team 2|>
</center>
|>

<style>
  /* Default button style (for light mode) /
  .button {
    background-color: white;
    color: black;
  }

  / Media query for dark mode */
@media (prefers-color-scheme: dark) {
    .button {
      background-color: black;
      color: white;
    }
}

@media (prefers-color-scheme: dark) {
    .card {
      background-color: #994eba;
      color: white;
    }
}
</style>
<br/>
<|Generate Visualization|button|on_action=button_pressed|class_name=button|>
|>