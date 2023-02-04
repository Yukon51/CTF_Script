<?php 
@session_start(); 
@set_time_limit(0); 
@error_reporting(0); 
function encode($D,$K){ 
    for($i=0;$i<strlen($D);$i++) { 
        $c = $K[$i+1&15]; 
        $D[$i] = $D[$i]^$c; 
    } 
    return $D; 
}
$key='3c6e0b8a9c15224a';

$data=substr("72a9c691ccdaab98fL1tMGI4YTljMn75e3jOBS5/V31Qd1NxKQMCe3h4KwFQfVAEVworCi0FfgB+BlWZhjRlQuTIIB5jMTU=b4c4e1f6ddd2a488",16, -16);
// $data='J+5pNzMyNmU2mij7dMD/qHMAa1dTUh6rZrUuY2l7eDVot058H+AZShmyrB3w/OdLFa2oeH/jYdeYr09l6fxhLPMsLeAwg8MkGmC+Nbz1+kYvogF0EFH1p/KFEzIcNBVfDaa946G+ynGJob9hH1+WlZFwyP79y4/cvxxKNVw8xP1OZWE3';
// $data = "fL1tMGI4YTljMX78f8Wo/yhTh1ICWCl3T2Dlffl9LdSpe0j5qneQcq98UNA0fsVlxxBe14XeR9/GMTU0pI7iA2M2ZQ==";

// echo encode(base64_decode($data), $key);
echo gzdecode(encode(base64_decode($data), $key));
?>