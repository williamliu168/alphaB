<!DOCTYPE html>
<html>
<body>

<?php
    include("ts.php");

    $ts = new timeSerie;
    $ts->addPoint("EPS",array(1,3,2,4,3,5,4,7,6,8,6,10,6.5,15));
    // $ts->display();
    
?>
    <img src="chart.php?x=300">

</body>
</html>