var player;
var lecture_list;

/*
	This function will look for the viewer screen ratio and adjust the player ratio with it.
	'interactive' command will adjust screen and video player ratio at once.
*/		
document.onreadystatechange = function(){
	if (document.readyState == 'interactive') {		
		player = document.getElementById('player')
		lecture_list = document.getElementById('lecture_list')
    	maintainRatio()
	}
}

// maintainRatio function will maintain the ratio of the player a/c to the display size.
function maintainRatio(){
	var w = player.clientWidth
    var h = (w*9)/16           // 16/9 is the ratio of the youtube video player
    player.height = h
	console.log({w, h});
	lecture_list.style.maxHeight = h + "px"   // This will set the height of lecture list same as the height of player

}

window.onresize = maintainRatio
    	