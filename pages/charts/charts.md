<br/>
<br/>
<|part|render={showGraphs}|
<center>
<|{selected_team}|toggle|lov={values}|on_change=toggle_choice|>
</center>
<|{data}|chart|type=pie|values=Count|labels=Country|>
<|{df}|chart|type=bar|x=Season|y[1]=W|y[2]=L|>

|>