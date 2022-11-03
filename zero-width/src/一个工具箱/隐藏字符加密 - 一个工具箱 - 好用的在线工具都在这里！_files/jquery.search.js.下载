//  绑定搜索输入框
function HtmlBind_Search() {
    $("#btnSearch").click(function(){
		var keyword = $("#txtSearch").val();
        if (keyword == "") return;
        var URL = "./Search.php?Keyword=" + keyword;
        location.href = URL;
	});

    // $("#txtSearch").keypress(function (e) {
    //     var keycode = (e.keyCode ? e.keyCode : e.which);
    //     if (keycode == 13) {
    //         var keyword = $("txtSearch").val();
    //         if (keyword == "") return;
    //         var URL = "./Search.php?Keyword=" + keyword;
    //         location.href = URL;
    //     }
    // });

    // 淘宝优惠券搜索
    $("#btnCouponsSearch").click(function(){
		var keyword = $("#txtKeyword").val();
        if (keyword == "") return;
        var URL = "./Tool.php?Id=741&k=" + keyword;
        location.href = URL;
    });
    
    $("#txtKeyword").keypress(function (e) {
        var keycode = (e.keyCode ? e.keyCode : e.which);
        if (keycode == 13) {
            var keyword = $("#txtKeyword").val();
            if (keyword == "") return;
            var URL = "./Tool.php?Id=741&k=" + keyword;
            location.href = URL;
        }
    });

    // 淘宝搜索
    $("#btnSalesSearch").click(function(){
		var keyword = $("#txtSalesKeyword").val();
        if (keyword == "") return;
        var URL = "./Tool.php?Id=798&k=" + keyword;
        if (isMobile()) {
            URL = "https://temai.m.taobao.com/search.htm?pid=mm_11125958_291350144_83836250300&union_lens=lensId%3APUB%401616330957%400b092bc3_0ee4_17854d52191_03fd%4001&q=" + keyword;
        } else {
            URL = "https://ai.taobao.com/search/index.htm?pid=mm_11125958_291350144_83836250300&union_lens=lensId%3APUB%401616331036%400b081316_0eaa_17854d65913_03f3%4001&key=" + keyword;
        }
        // location.href = URL;
        window.open(URL);
    });
    
    $("#txtSalesKeyword").keypress(function (e) {
        var keycode = (e.keyCode ? e.keyCode : e.which);
        if (keycode == 13) {
            var keyword = $("#txtSalesKeyword").val();
            if (keyword == "") return;
            var URL = "./Tool.php?Id=798&k=" + keyword;
            if (isMobile()) {
                URL = "https://temai.m.taobao.com/search.htm?pid=mm_11125958_291350144_83836250300&union_lens=lensId%3APUB%401616330957%400b092bc3_0ee4_17854d52191_03fd%4001&q=" + keyword;
            } else {
                URL = "https://ai.taobao.com/search/index.htm?pid=mm_11125958_291350144_83836250300&union_lens=lensId%3APUB%401616331036%400b081316_0eaa_17854d65913_03f3%4001&key=" + keyword;
            }
            // location.href = URL;
            window.open(URL);
        }
    });
}

// 绑定“我的工具”点击事件
function Bind_My() {
    var myToolboxId = '';

    if(isEmpty(store.get('atoolbox-my-toolbox'))) {
        return false;
    } else {
        myToolboxId = store.get('atoolbox-my-toolbox').id;
        if(isEmpty(myToolboxId)) {
            return false;
        } else {
            window.location.href = './My.php?Id=' + myToolboxId;
        }
    }
}