<?php
    // $data = $_GET['data_point']
    $data = array();
    $d = 100;
    for($i=0;$i<400;$i++)
    {
        $delta = (mt_rand(-30,30)+1)/1000;
        $d=$d*(1+$delta);
        array_push($data,$d);
    }
    
    $n = count($data);
    
    $max_x = 800;
    $max_y = 200;
    
    $marginPct = 3;
    $margin_x = ceil($max_x*$marginPct/100);
    $margin_y = ceil($max_y*$marginPct/100);
    
    $chart_area_x0 = $margin_x;
    $chart_area_y0 = $max_y-$margin_y;
    $chart_area_xt = $max_x-$margin_x;
    $chart_area_yt = $margin_y;
    $chart_width = abs($chart_area_xt-$chart_area_x0);
    $chart_height = abs($chart_area_yt-$chart_area_y0);
    
    $interval_x = $chart_width/$n;
    $data_min_y = min($data);
    $data_max_y = max($data);
    $range_y = ($data_max_y-$data_min_y)/0.8;
    $data_y_start = $data_min_y-($range_y-($data_max_y-$data_min_y))/2;
    $data_y_end = $data_y_start+$range_y;
    
    $interval_y = $chart_height/$range_y;
    
    header ('Content-Type: image/png');
    $im = @imagecreatetruecolor($max_x, $max_y) or die('Cannot Initialize new GD image stream');
    
    
    $white = imagecolorallocate($im,255,255,255);
    $black = imagecolorallocate($im,0,0,0);
    $lightgrey = imagecolorallocate($im,233,233,233);
    $red = imagecolorallocate($im,231, 76, 60);
    $green = imagecolorallocate($im,88, 214, 141);
    
    imagefill($im,0,0,$lightgrey);
    
    imagerectangle($im, $margin_x, $margin_y, $max_x-$margin_x, $max_y-$margin_y, $black);
    
    $i = 0;
    foreach ($data as $point)
    {
        $x = $margin_x+$interval_x*($i+0.5);
        $y = $max_y-($margin_y+$interval_y*($point-$data_y_start));
        
        if (isset($prev_x)&&isset($prev_y))
        {
            $lineColor = $black;
            if ($y<$prev_y)
            {
                $lineColor=$green;
            }
            else if ($y==$prev_y)
            {
                $lineColor=$black;
            }
            else
            {
                $lineColor=$red;
            }
            imageline( $im, $x, $y, $prev_x, $prev_y, $lineColor );
        }

        // imagesetpixel( $im, $interval_x*($i+0.5), 150, $black);
        // imagesetpixel( $im, $x, $y, $black);
        $i=$i+1;
        
        $prev_x = $x;
        $prev_y = $y;
    }
    
    // imagestring( $im, 1, 15, 15, $margin_x , $black);
    // imagestring( $im, 1, 15, 25, $margin_y , $black);
    // imagestring( $im, 1, 15, 35, $margin_y , $black);
    
    imagepng($im);
    imagedestroy($im);
?>