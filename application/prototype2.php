<!DOCTYPE html>
<html>
    <body>
    <link rel="stylesheet" href="css/main.css" />
        <script type = "text/javascript">
            const times = [];
            let fps;
            function refreshLoop() {
                window.requestAnimationFrame(() => {
                    const now = performance.now();
                    while (times.length > 0 && times[0] <= now - 1000) {
                        times.shift();
                    }
                times.push(now);
                fps = times.length;
                kFps2.style.color = "black"
                kFps2.textContent = fps
                kpFps2.value = fps
                refreshLoop();
                });
            }
            refreshLoop();    
        </script><h1>Prototype</h1>
        <table style="width:100%">
            <tr>
                <td>FPS</td>
                <td><span id="kFps2"></span>
                    <progress id="kpFps2" value="0" min="0" max="100" style="vertical-align:middle"></progress></td>
            </tr>
            <tr>
                <td>Location</td>
                <td>drone/edge/cloud</td>
            </tr>
            <tr>
                <td>Ping</td>
                <td>0 ms</td>
            </tr>
            <tr>
                <td>CPU use</td>
                <td><?php
$output = shell_exec('wmic cpu get loadpercentage');
echo "<pre>$output</pre>";
?></td>
            </tr>
            <tr>
                <td>GPU use</td>
                <td><form method="post"><input type="submit" name="test" id="test" value="RUN" /><br/>
</form>
<?php

function testfun()
{
    shell_exec('taskmgr');
}

if(array_key_exists('test',$_POST)){
   testfun();
}

?></td>
            </tr>
            <tr>
                <td>Battery use</td>
                <td>xx%</td>
            </tr>
        </table>
        <video autoplay playsinline></video>
        <script src = "js/main.js"></script>
        <!--<iframe src="https://www.ustream.tv/embed/23671967?html5ui" style="border: 0;" webkitallowfullscreen allowfullscreen frameborder="no" width="480" height="270"></iframe>-->
    </body>
</html>