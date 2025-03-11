var vigeniere= vigeniere || (function(){
    var proceso= function(txt, desp, action){
        var replace = ( function(){
            var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
            var longitud= abc.length;
            return function(c){
                var i= abc.indexOf(c.toLowerCase());
                if(i!= -1){
                    var pos =i;
                    if(action){
                        pos += desp;
                        pos = (pos >= longitud)? pos -1 : pos; 

                    }else{

                    }
                    return abc[pos];
                }
                return c;
            }
        })
    }
})