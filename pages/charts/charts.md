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
<|{data}|chart|type=pie|values=Count|labels=Country|>
|>
<|part|render={showGraphs}|
<|{dataframe}|chart|type=bar|x=Season|y[1]=W|y[2]=L|layout={layout}|>
|>
|>