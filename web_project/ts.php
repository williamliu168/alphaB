<?php

class timeSerie
{
    public $start = '';
    public $end = '';
    public $title = '';
    
    public $data = array();
    
    function __construct() {
       print("creating new timeSerie\n");
       $this->title = "hello";
   }
    
    function display()
    {
        print_r($this->data);
    }
    
    function addPoint($in_title,$in_points)
    {
        $this->title = $in_title;
        $this->data = $in_points;
    }
    
    function paintSelf()
    {

    }
}

class tsDataPoint
{
    public $timestamp;
    public $data = array();
    
    function display()
    {
        print_r($data);
    }
}

?>