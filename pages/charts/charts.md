<br/>
<br/>
<|part|render={showToggles}|
<center>
<|{selected_team}|toggle|lov={values}|on_change=toggle_choice|>
</center>
|>
<br/>
<|layout|column=1 1|
<|part|render={showGraphs}|
<|{data}|chart|type=pie|values=Count|labels=Country|title=Percentage of Players by Nationality|>
|>
<|part|render={showGraphs}|
<|{dataframe}|chart|type=bar|x=Season|y[1]=W|y[2]=L|layout={layout}|>
|>
|>
<br/>
<|part|render={showGraphs}|
<|{allFrame}|chart|mode=lines|x=Season|y[1]=Goals Scored|y[2]=Goals Conceded|y[3]=Points|>
|>