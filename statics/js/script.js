// like a post


function likePost(e, id, code){
	var itag = e.querySelector("i")
	var classes = itag.classList

	if (!classes.contains("likedButton")){
		classes.remove("ti-heart")
		classes.add("likedButton")

		itag.innerText = "❤️"
		e.querySelector("ins").innerText = Number(e.querySelector("ins").innerText) + 1 

	}
	else{
		classes.remove("likedButton")
		classes.add("ti-heart")

		itag.innerText = ""
		e.querySelector("ins").innerText = Number(e.querySelector("ins").innerText) - 1 
	}
	if (code)
		{$.ajax({
			url: "/likePost",
			method: "POST",
			data: {
				"id": id,
				"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]")[0].value,
			},
		});	
	}
}



jQuery(document).ready(function($) {
	
	"use strict";
	
//------- Notifications Dropdowns
  $('.top-area > .setting-area > li').on("click",function(){
	$(this).siblings().children('div').removeClass('active');
	$(this).children('div').addClass('active');
	return false;
  });
//------- remove class active on body
  $("body *").not('.top-area > .setting-area > li').on("click", function() {
	$(".top-area > .setting-area > li > div").removeClass('active');		
 });
	

//--- user setting dropdown on topbar	
$('.userInfo').on('click', function() {
	$('.user-setting').toggleClass("active");
	return false;
});	

//--------- change user status
$('.set-offline').on('click', function(){
	$('.user-img span')[0].className = "status f-off"
	$('.user-img span')[1].className = "status f-off"
});	
$('.set-online').on('click', function(){
	$('.user-img span')[0].className = "status f-online"
	$('.user-img span')[1].className = "status f-online"
});	
$('.set-away').on('click', function(){
	$('.user-img span')[0].className = "status f-away"
	$('.user-img span')[1].className = "status f-away"
});	
$('.view-profile').on('click', function(){
	window.location.href = window.location.origin + "/timeline?u=" + document.getElementById("userUsername").innerText;
});
$('.edit-profile').on('click', function(){
	window.location.href = window.location.origin + "/edit-profile";
});
$('.logout').on('click', function(){
	window.location.href = window.location.origin + "/logout";
});


//--- side message box	
// $('.friendz-list > li, .chat-users > li').on('click', function() {
// 	$('.chat-box').addClass("show");
// 	return false;
// });	
	$('.close-mesage').on('click', function() {
		$('.chat-box').removeClass("show");
		return false;
	});	
	
//------ scrollbar plugin
	if ($.isFunction($.fn.perfectScrollbar)) {
		$('.dropdowns, .twiter-feed, .invition, .followers, .chatting-area, .peoples, #people-list, .chat-list > ul, .message-list, .chat-users, .left-menu').perfectScrollbar();
	}

/*--- socials menu scritp ---*/	
	$('.trigger').on("click", function() {
	    $(this).parent(".menu").toggleClass("active");
	  });
	
/*--- emojies show on text area ---*/	
	$('.add-smiles > span').on("click", function() {
	    $(this).parent().siblings(".smiles-bunch").toggleClass("active");
	  });

// delete notifications
$('.notification-box > ul li > i.del').on("click", function(){
    $(this).parent().slideUp();
	return false;
  }); 	

/*--- socials menu scritp ---*/	
	$('.f-page > figure i').on("click", function() {
	    $(".drop").toggleClass("active");
	  });

//===== Search Filter =====//
	(function ($) {
	// custom css expression for a case-insensitive contains()
	jQuery.expr[':'].Contains = function(a,i,m){
	  return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase())>=0;
	};

	function listFilter(searchDir, list) { 
	  var form = $("<form>").attr({"class":"filterform","action":"#"}),
	  input = $("<input>").attr({"class":"filterinput","type":"text","placeholder":"Search Contacts..."});
	  $(form).append(input).appendTo(searchDir);

	  $(input)
	  .change( function () {
		var filter = $(this).val();
		if(filter) {
		  $(list).find("li:not(:Contains(" + filter + "))").slideUp();
		  $(list).find("li:Contains(" + filter + ")").slideDown();
		} else {
		  $(list).find("li").slideDown();
		}
		return false;
	  })
	  .keyup( function () {
		$(this).change();
	  });
	}

//search friends widget
	$(function () {
	  listFilter($("#searchDir"), $("#people-list"));
	});
	}(jQuery));	

//progress line for page loader
	$('body').show();
	NProgress.start();
	setTimeout(function() { NProgress.done(); $('.fade').removeClass('out'); }, 2000);
	
//--- bootstrap tooltip	
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip();
	});
	
// Sticky Sidebar & header
	if($(window).width() < 769) {
		jQuery(".sidebar").children().removeClass("stick-widget");
	}

	if ($.isFunction($.fn.stick_in_parent)) {
		$('.stick-widget').stick_in_parent({
			parent: '#page-contents',
			offset_top: 60,
		});

		
		$('.stick').stick_in_parent({
		    parent: 'body',
            offset_top: 0,
		});
		
	}
	
/*--- topbar setting dropdown ---*/	
	$(".we-page-setting").on("click", function() {
	    $(".wesetting-dropdown").toggleClass("active");
	  });	
	  
/*--- topbar toogle setting dropdown ---*/	
$('#nightmode').on('change', function() {
    if ($(this).is(':checked')) {
        // Show popup window
        $(".theme-layout").addClass('black');	
    }
	else {
        $(".theme-layout").removeClass("black");
    }
});

//chosen select plugin
if ($.isFunction($.fn.chosen)) {
	$("select").chosen();
}

//----- add item plus minus button
if ($.isFunction($.fn.userincr)) {
	$(".manual-adjust").userincr({
		buttonlabels:{'dec':'-','inc':'+'},
	}).data({'min':0,'max':20,'step':1});
}	
	
if ($.isFunction($.fn.loadMoreResults)) {	
	$('.loadMore').loadMoreResults({
		displayedItems: 3,
		showItems: 2,
		button: {
		  'class': 'btn-load-more',
		  'text': 'Load More'
		}
	});	
}
	//===== owl carousel  =====//
	if ($.isFunction($.fn.owlCarousel)) {
		$('.sponsor-logo').owlCarousel({
			items: 6,
			loop: true,
			margin: 30,
			autoplay: true,
			autoplayTimeout: 1500,
			smartSpeed: 1000,
			autoplayHoverPause: true,
			nav: false,
			dots: false,
			responsiveClass:true,
				responsive:{
					0:{
						items:3,
					},
					600:{
						items:3,

					},
					1000:{
						items:6,
					}
				}

		});
	}
	
// slick carousel for detail page
	if ($.isFunction($.fn.slick)) {
	$('.slider-for-gold').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		slide: 'li',
		fade: false,
		asNavFor: '.slider-nav-gold'
	});
	
	$('.slider-nav-gold').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		asNavFor: '.slider-for-gold',
		dots: false,
		arrows: true,
		slide: 'li',
		vertical: true,
		centerMode: true,
		centerPadding: '0',
		focusOnSelect: true,
		responsive: [
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				vertical: false,
				centerMode: true,
				dots: false,
				arrows: false
			}
		},
		{
			breakpoint: 641,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				vertical: true,
				centerMode: true,
				dots: false,
				arrows: false
			}
		},
		{
			breakpoint: 420,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				vertical: false,
				centerMode: true,
				dots: false,
				arrows: false
			}
		}	
		]
	});
}
	
//---- responsive header
	
$(function() {

	//	create the menus
	$('#menu').mmenu();
	$('#shoppingbag').mmenu({
		navbar: {
			title: 'General Setting'
		},
		offCanvas: {
			position: 'right'
		}
	});

	//	fire the plugin
	$('.mh-head.first').mhead({
		scroll: {
			hide: 200
		}
		
	});
	$('.mh-head.second').mhead({
		scroll: false
	});

	
});		

//**** Slide Panel Toggle ***//
	  $("span.main-menu").on("click", function(){
	    $(".side-panel").addClass('active');
		$(".theme-layout").addClass('active');

		  return false;
	  });

	  $('.theme-layout').on("click",function(){
		  $(this).removeClass('active');
	     $(".side-panel").removeClass('active');
		  
	     
	  });

	  
// login & register form
	$('button.signup').on("click", function(){
		$('.login-reg-bg').addClass('show');
		return false;
	  });
	  
	  $('.already-have').on("click", function(){
		$('.login-reg-bg').removeClass('show');
		return false;
	  });
	
//----- count down timer		
	if ($.isFunction($.fn.downCount)) {
		$('.countdown').downCount({
			date: '11/12/2018 12:00:00',
			offset: +10
		});
	}
	
/** Post a Comment **/
jQuery(".post-comt-box textarea").on("keydown", function(event) {

	if (event.keyCode == 13) {
		var comment = jQuery(this).val();
		var parent = jQuery(".showmore").parent("li");
		var comment_HTML = '	<li><div class="comet-avatar"><img src="images/resources/comet-1.jpg" alt=""></div><div class="we-comment"><div class="coment-head"><h5><a href="time-line.html" title="">Jason borne</a></h5><span>1 year ago</span><a class="we-reply" href="#" title="Reply"><i class="fa fa-reply"></i></a></div><p>'+comment+'</p></div></li>';
		$(comment_HTML).insertBefore(parent);
		jQuery(this).val('');
	}
}); 
	
//inbox page 	
//***** Message Star *****//  
    $('.message-list > li > span.star-this').on("click", function(){
    	$(this).toggleClass('starred');
    });


//***** Message Important *****//
    $('.message-list > li > span.make-important').on("click", function(){
    	$(this).toggleClass('important-done');
    });

    

// Listen for click on toggle checkbox
	$('#select_all').on("click", function(event) {
	  if(this.checked) {
	      // Iterate each checkbox
	      $('input:checkbox.select-message').each(function() {
	          this.checked = true;
	      });
	  }
	  else {
	    $('input:checkbox.select-message').each(function() {
	          this.checked = false;
	      });
	  }
	});


	$(".delete-email").on("click",function(){
		$(".message-list .select-message").each(function(){
			  if(this.checked) {
			  	$(this).parent().slideUp();
			  }
		});
	});

// change background color on hover
	$('.category-box').hover(function () {
		$(this).addClass('selected');
		$(this).parent().siblings().children('.category-box').removeClass('selected');
	});
	
	
//------- offcanvas menu 

	const menu = document.querySelector('#toggle');  
	const menuItems = document.querySelector('#overlay');  
	const menuContainer = document.querySelector('.menu-container');  
	const menuIcon = document.querySelector('.canvas-menu i');  

	function toggleMenu(e) {
		menuItems.classList.toggle('open');
		menuContainer.classList.toggle('full-menu');
		menuIcon.classList.toggle('fa-bars');
		menuIcon.classList.add('fa-times');
		e.preventDefault();
	}

	if( menu ) {
		menu.addEventListener('click', toggleMenu, false);	
	}
	
// Responsive nav dropdowns
	$('.offcanvas-menu li.menu-item-has-children > a').on('click', function () {
		$(this).parent().siblings().children('ul').slideUp();
		$(this).parent().siblings().removeClass('active');
		$(this).parent().children('ul').slideToggle();
		$(this).parent().toggleClass('active');
		return false;
	});	
	

	const chatSocket = new WebSocket(
	'ws://'
	+ window.location.host
	+ '/ws/messages/{{toChat.username}}/'
	);
	window.chatSocket = chatSocket

	chatSocket.onclose = function(e) {
		console.error('Chat socket closed unexpectedly');
	};
	var flag = 1
	var lastSearch = ""
	$("input[name='searchUser']").keyup((e) =>{
		if (flag && lastSearch != e.target.value){
			console.log("lakd")
			flag = 0
			lastSearch = e.target.value
			var container = document.getElementsByClassName("nearby-contct")[0]
			if (lastSearch.length < 1){
				container.style.display = "none"
				flag = 1
				return
			}
			else{
				container.style.display = "inline-block"
			} 
			container.innerHTML = ""

			setTimeout(flag=1, 1000)
			$.ajax({
				url: "/searchUser",
				method: "POST",
				data: {
					"searched": lastSearch,
					"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]")[0].value,
				},
				success: function(ret){
					ret = JSON.parse(ret).ret
					var code = `<li>\
					<div class="nearly-pepls">\
							<figure>\
								<a href="" title=""><img src="" alt=""></a>\
							</figure>\
							<div class="pepl-info">\
								<h4><a href="" title=""></a></h4>\
								<a href="#" title="" username="" class="addFriend add-butn" data-ripple="" onclick="this.innerText = 'Added Friend'; window.addfriendrequest(this)">Add Friend</a>\
							</div>\
						</div>\
					</li>`

					for(var i=0; i<ret.length; i++){
						container.innerHTML += code
						var latest_block = container.getElementsByTagName("li")[i]
						latest_block.getElementsByTagName("img")[0].src = ret[i].imageURL
						latest_block.getElementsByClassName("pepl-info")[0].getElementsByTagName("a")[0].innerText = ret[i].fullname
						latest_block.getElementsByClassName("pepl-info")[0].getElementsByTagName("a")[0].href = "/timeline?u="+ret[i].username
						latest_block.getElementsByClassName("pepl-info")[0].getElementsByTagName("a")[1].setAttribute("username", ret[i].username)
						latest_block.getElementsByTagName("figure")[0].getElementsByTagName("a").href = "/timeline?u="+ret[i].username

					}
				}
			});
		}
	})

});//document ready end





