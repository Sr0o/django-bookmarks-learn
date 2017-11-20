(function () {
	var jquery_version = '3.2.1';
	var site_url = 'http://192.168.1.103:8000/';
	var static_url = site_url + 'static/';
	var min_width = 100;
	var min_height = 100;

	function bookmarklet(msg) {
		var css = jQuery('<link>');
		css.attr({
			rel: 'stylesheet',
			type: 'text/css',
			href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random() * 99999999999999999999)
		});
		jQuery('head').append(css);

		box_html = '<div id="bookmarklet"><a href="#" id="close">x</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
		jQuery('body').append(box_html);

		jQuery('#bookmarklet #close').click(function () {
			jQuery('#bookmarklet').remove();
		});
		
		jQuery.each(jQuery('img[src$="jpg"]'), function (index, image) {
			if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height) {
				image_url = jQuery(image).attr('src');
				jQuery('#bookmarklet .images').append('<a href="#"><img src="' + image_url + '" /></a>');
			}
		});

		jQuery('#bookmarklet .images a').click(function (e) {
			selected_image = jQuery(this).children('img').attr('src');
			jQuery('#bookmarklet').hide();
			window.open(site_url + 'images/create/?url=' + encodeURIComponent(selected_image) + '&title=' + encodeURIComponent(jQuery('title').text()), '_blank');
		});
	};

	if (typeof window.jQuery !== 'undefined') {/* typeof---'undefined' 或 undefined*/
		bookmarklet();
	} else {
		var conflict = typeof window.$ !== 'undefined';
		var script = document.createElement('script');
		script.setAttribute('src', 'https://code.jquery.com/jquery-' + jquery_version + '.min.js');
		document.getElementsByTagName('head')[0].appendChild(script);
		var attempts = 15;
		(function () {
			if (typeof window.jQuery === 'undefined') {
				if (--attempts > 0) {
					window.setTimeout(arguments.callee, 250)
				} else {
					alert('An error ocurred while loading jQuery')
				}
			} else {
				bookmarklet();
			}
		})();
	}
})()
