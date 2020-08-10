(function() {
  // JS practice.
  // Reference：https://codepen.io/supah/pen/jqOBqp
  // It's Cool ! ↑
  var fakeMsg, fakeNum, isTyping, messages, uctTimer;
  let nombre, estado,conciencia

  //Setup establecido
  fetch('/setup')
  .then( res => res.json())
  .then( data => {
    nombre = data[0]
    estado = data[1]
    conciencia = data[2]
    console.log("Setup->:"+data);
    }).catch(error =>{
    console.log('Se ha encontrado un error en el archivo o web que se hace la peticion');
  })
  messages = $(".messages-content");

  fakeNum = 0;

  isTyping = true;

  uctTimer = null;

  window.userTypingClear = function() {
    return uctTimer = setTimeout(function() {
      $(".message.personal.typing").remove();
      return isTyping = true;
    }, 3500);
  };
  window.setDate = function() {
    var d, timestamp;
    timestamp = $("<div>").addClass("timestamp");
    d = new Date();
    timestamp.text(d.getHours() + ":" + (d.getMinutes() < 10 ? '0' : '') + d.getMinutes());
    return timestamp.appendTo($('.message:last'));
  };

  window.updateScrollbar = function() {
    return messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
      scrollInertia: 10,
      timeout: 0
    });
  };
   //console.log( {{ setup }} )
  fakeMsg = ["Hola, me dicen Serome y tu como te llamas?"," Mucho gusto "," ¿Cómo te va? "," Bastante bien "," ¿Cómo te ha estado tratando la vida? "," Podría ser peor. "," Tengo que irme ahora "," Fue un placer conversar contigo "," Adiós :)"];
  let cont=0;
  window.setFakeMessage = function(palabra) {
    var typing;
    typing = $("<div>").append("<span>").addClass("message  typing");
    typing.appendTo($('.mCSB_container'));
    updateScrollbar();
    return setTimeout(function() {
      var msg;
      typing.remove();
      msg = $("<div>").addClass("message");
      
      if(cont == 0){

        var datos = new FormData();
        datos.append('palabra', palabra);

        fetch('/get_data',{
          method: 'POST',
          body: datos
         })
        .then( res => res.json())
        .then( data => {
          if(data[0] === 'url'){
            //console.log('Redireccionando');
            window.location.href = "/";
          }
          console.log("el-fetch->:"+data);
          }).catch(error =>{
          console.log('Se ha encontrado un error en el archivo o web que se hace la peticion');
        })
        

      }
      msg.text(fakeMsg[fakeNum]);
      //msg.text('palabra');
      msg.appendTo($('.mCSB_container'));
      setDate();
      updateScrollbar();
      return fakeNum++;
    }, 1000 + (Math.random() * 10) * 100);
  };

  window.insertMessage = function() {
    var msg, msgText;
    msgText = $(".action-box-input").val();
    if ($.trim(msgText) === "") {
      return false;
    }
    msg = $("<div>").addClass("message");
    msg.text(msgText);
    msg.addClass("personal").appendTo($('.mCSB_container'));
    setDate();
    updateScrollbar();
    $(".action-box-input").val(null);
    $(".message.personal.typing").remove();
    isTyping = true;
    clearTimeout(uctTimer);
    if ($.trim(fakeMsg[fakeNum]) === "") {
      return false;
    }
    return setTimeout(function() {
      return setFakeMessage(msgText);
    }, 500 + (Math.random() * 10) * 100);
  };

  $(window).on('keydown', function(e) {
    if (e.which === 13) {
      insertMessage();
      return false;
    }
  });

  $(window).load(function() {
    messages.mCustomScrollbar();
    setTimeout(function() {
      return setFakeMessage();
    }, 100);
  });

  $(".action-box-input").on("keydown", function(e) {
    var typing;
    if ($(".action-box-input") !== "" && isTyping === true && e.which !== 13) {
      typing = $("<div>").append("<span>").addClass("message personal typing");
      typing.appendTo($('.mCSB_container'));
      updateScrollbar();
      isTyping = false;
      return userTypingClear();
    }
  });

}).call(this);

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiPGFub255bW91cz4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFBQTs7O0FBQUEsTUFBQSxPQUFBLEVBQUEsT0FBQSxFQUFBLFFBQUEsRUFBQSxRQUFBLEVBQUE7O0VBSUEsUUFBQSxHQUFXLENBQUEsQ0FBRSxtQkFBRjs7RUFDWCxPQUFBLEdBQVU7O0VBRVYsUUFBQSxHQUFXOztFQUNYLFFBQUEsR0FBVzs7RUFFWCxNQUFNLENBQUMsZUFBUCxHQUF5QixRQUFBLENBQUEsQ0FBQTtXQUN4QixRQUFBLEdBQVcsVUFBQSxDQUFXLFFBQUEsQ0FBQSxDQUFBO01BQ3JCLENBQUEsQ0FBRSwwQkFBRixDQUE2QixDQUFDLE1BQTlCLENBQUE7YUFDQSxRQUFBLEdBQVc7SUFGVSxDQUFYLEVBR1QsSUFIUztFQURhOztFQU16QixNQUFNLENBQUMsT0FBUCxHQUFpQixRQUFBLENBQUEsQ0FBQTtBQUNoQixRQUFBLENBQUEsRUFBQTtJQUFBLFNBQUEsR0FBWSxDQUFBLENBQUUsT0FBRixDQUFVLENBQUMsUUFBWCxDQUFvQixXQUFwQjtJQUNaLENBQUEsR0FBSSxJQUFJLElBQUosQ0FBQTtJQUNKLFNBQVMsQ0FBQyxJQUFWLENBQWUsQ0FBQyxDQUFDLFFBQUYsQ0FBQSxDQUFBLEdBQWUsR0FBZixHQUFxQixDQUFJLENBQUMsQ0FBQyxVQUFGLENBQUEsQ0FBQSxHQUFpQixFQUFwQixHQUE0QixHQUE1QixHQUFxQyxFQUF0QyxDQUFyQixHQUFpRSxDQUFDLENBQUMsVUFBRixDQUFBLENBQWhGO1dBQ0EsU0FBUyxDQUFDLFFBQVYsQ0FBbUIsQ0FBQSxDQUFFLGVBQUYsQ0FBbkI7RUFKZ0I7O0VBTWpCLE1BQU0sQ0FBQyxlQUFQLEdBQXlCLFFBQUEsQ0FBQSxDQUFBO1dBQ3ZCLFFBQVEsQ0FBQyxnQkFBVCxDQUEwQixRQUExQixDQUFtQyxDQUFDLGdCQUFwQyxDQUFxRCxVQUFyRCxFQUFpRSxRQUFqRSxFQUNFO01BQUEsYUFBQSxFQUFlLEVBQWY7TUFDQSxPQUFBLEVBQVM7SUFEVCxDQURGO0VBRHVCOztFQUt6QixPQUFBLEdBQVUsQ0FDVCwrQkFEUyxFQUVULGtCQUZTLEVBR1Qsb0JBSFMsRUFJVCxhQUpTLEVBS1QsZ0NBTFMsRUFNVCwyQkFOUyxFQU9ULG9CQVBTLEVBUVQsaUNBUlMsRUFTVCxRQVRTOztFQVlWLE1BQU0sQ0FBQyxjQUFQLEdBQXdCLFFBQUEsQ0FBQSxDQUFBO0FBQ3ZCLFFBQUE7SUFBQSxNQUFBLEdBQVMsQ0FBQSxDQUFFLE9BQUYsQ0FBVSxDQUFDLE1BQVgsQ0FBa0IsUUFBbEIsQ0FBMkIsQ0FBQyxRQUE1QixDQUFxQyxnQkFBckM7SUFDVCxNQUFNLENBQUMsUUFBUCxDQUFnQixDQUFBLENBQUUsaUJBQUYsQ0FBaEI7SUFDQSxlQUFBLENBQUE7V0FDQSxVQUFBLENBQVcsUUFBQSxDQUFBLENBQUE7QUFDVixVQUFBO01BQUEsTUFBTSxDQUFDLE1BQVAsQ0FBQTtNQUNBLEdBQUEsR0FBTSxDQUFBLENBQUUsT0FBRixDQUFVLENBQUMsUUFBWCxDQUFvQixTQUFwQjtNQUNOLEdBQUcsQ0FBQyxJQUFKLENBQVMsT0FBUSxDQUFBLE9BQUEsQ0FBakI7TUFDQSxHQUFHLENBQUMsUUFBSixDQUFhLENBQUEsQ0FBRSxpQkFBRixDQUFiO01BQ0EsT0FBQSxDQUFBO01BQ0EsZUFBQSxDQUFBO2FBQ0EsT0FBQTtJQVBVLENBQVgsRUFRRSxJQUFBLEdBQU8sQ0FBQyxJQUFJLENBQUMsTUFBTCxDQUFBLENBQUEsR0FBZ0IsRUFBakIsQ0FBQSxHQUF1QixHQVJoQztFQUp1Qjs7RUFjeEIsTUFBTSxDQUFDLGFBQVAsR0FBdUIsUUFBQSxDQUFBLENBQUE7QUFDdEIsUUFBQSxHQUFBLEVBQUE7SUFBQSxPQUFBLEdBQVcsQ0FBQSxDQUFFLG1CQUFGLENBQXNCLENBQUMsR0FBdkIsQ0FBQTtJQUNYLElBQUcsQ0FBQyxDQUFDLElBQUYsQ0FBTyxPQUFQLENBQUEsS0FBbUIsRUFBdEI7QUFDQyxhQUFPLE1BRFI7O0lBRUEsR0FBQSxHQUFNLENBQUEsQ0FBRSxPQUFGLENBQVUsQ0FBQyxRQUFYLENBQW9CLFNBQXBCO0lBQ04sR0FBRyxDQUFDLElBQUosQ0FBUyxPQUFUO0lBQ0EsR0FBRyxDQUFDLFFBQUosQ0FBYSxVQUFiLENBQXdCLENBQUMsUUFBekIsQ0FBa0MsQ0FBQSxDQUFFLGlCQUFGLENBQWxDO0lBQ0EsT0FBQSxDQUFBO0lBQ0EsZUFBQSxDQUFBO0lBQ0EsQ0FBQSxDQUFFLG1CQUFGLENBQXNCLENBQUMsR0FBdkIsQ0FBMkIsSUFBM0I7SUFFQSxDQUFBLENBQUUsMEJBQUYsQ0FBNkIsQ0FBQyxNQUE5QixDQUFBO0lBQ0EsUUFBQSxHQUFXO0lBQ1gsWUFBQSxDQUFhLFFBQWI7SUFFQSxJQUFHLENBQUMsQ0FBQyxJQUFGLENBQU8sT0FBUSxDQUFBLE9BQUEsQ0FBZixDQUFBLEtBQTRCLEVBQS9CO0FBQ0MsYUFBTyxNQURSOztXQUVBLFVBQUEsQ0FBVyxRQUFBLENBQUEsQ0FBQTthQUNWLGNBQUEsQ0FBQTtJQURVLENBQVgsRUFFRSxHQUFBLEdBQU0sQ0FBQyxJQUFJLENBQUMsTUFBTCxDQUFBLENBQUEsR0FBZ0IsRUFBakIsQ0FBQSxHQUF1QixHQUYvQjtFQWpCc0I7O0VBcUJ2QixDQUFBLENBQUUsTUFBRixDQUFTLENBQUMsRUFBVixDQUFhLFNBQWIsRUFBd0IsUUFBQSxDQUFDLENBQUQsQ0FBQTtJQUN0QixJQUFJLENBQUMsQ0FBQyxLQUFGLEtBQVcsRUFBZjtNQUNFLGFBQUEsQ0FBQTtBQUNBLGFBQU8sTUFGVDs7RUFEc0IsQ0FBeEI7O0VBS0EsQ0FBQSxDQUFFLE1BQUYsQ0FBUyxDQUFDLElBQVYsQ0FBZSxRQUFBLENBQUEsQ0FBQTtJQUNkLFFBQVEsQ0FBQyxnQkFBVCxDQUFBO0lBQ0EsVUFBQSxDQUFXLFFBQUEsQ0FBQSxDQUFBO2FBQ1YsY0FBQSxDQUFBO0lBRFUsQ0FBWCxFQUVFLEdBRkY7RUFGYyxDQUFmOztFQU9BLENBQUEsQ0FBRSxtQkFBRixDQUFzQixDQUFDLEVBQXZCLENBQTBCLFNBQTFCLEVBQXFDLFFBQUEsQ0FBQyxDQUFELENBQUE7QUFDcEMsUUFBQTtJQUFBLElBQUcsQ0FBQSxDQUFFLG1CQUFGLENBQUEsS0FBMEIsRUFBMUIsSUFBZ0MsUUFBQSxLQUFZLElBQTVDLElBQW9ELENBQUMsQ0FBQyxLQUFGLEtBQVcsRUFBbEU7TUFDQyxNQUFBLEdBQVMsQ0FBQSxDQUFFLE9BQUYsQ0FBVSxDQUFDLE1BQVgsQ0FBa0IsUUFBbEIsQ0FBMkIsQ0FBQyxRQUE1QixDQUFxQyx5QkFBckM7TUFDVCxNQUFNLENBQUMsUUFBUCxDQUFnQixDQUFBLENBQUUsaUJBQUYsQ0FBaEI7TUFDQSxlQUFBLENBQUE7TUFDQSxRQUFBLEdBQVc7YUFDWCxlQUFBLENBQUEsRUFMRDs7RUFEb0MsQ0FBckM7QUF0RkEiLCJzb3VyY2VzQ29udGVudCI6WyIjIEpTIHByYWN0aWNlLlxuIyBSZWZlcmVuY2XvvJpodHRwczovL2NvZGVwZW4uaW8vc3VwYWgvcGVuL2pxT0JxcFxuIyBJdCdzIENvb2wgISDihpFcblxubWVzc2FnZXMgPSAkKFwiLm1lc3NhZ2VzLWNvbnRlbnRcIilcbmZha2VOdW0gPSAwXG5cbmlzVHlwaW5nID0gdHJ1ZVxudWN0VGltZXIgPSBudWxsXG5cbndpbmRvdy51c2VyVHlwaW5nQ2xlYXIgPSAtPlxuXHR1Y3RUaW1lciA9IHNldFRpbWVvdXQgLT5cblx0XHQkKFwiLm1lc3NhZ2UucGVyc29uYWwudHlwaW5nXCIpLnJlbW92ZSgpXG5cdFx0aXNUeXBpbmcgPSB0cnVlXG5cdCwgMzUwMFxuXG53aW5kb3cuc2V0RGF0ZSA9IC0+XG5cdHRpbWVzdGFtcCA9ICQoXCI8ZGl2PlwiKS5hZGRDbGFzcyBcInRpbWVzdGFtcFwiXG5cdGQgPSBuZXcgRGF0ZSgpXG5cdHRpbWVzdGFtcC50ZXh0IGQuZ2V0SG91cnMoKSArIFwiOlwiICsgKGlmIGQuZ2V0TWludXRlcygpIDwgMTAgdGhlbiAnMCcgZWxzZSAnJykgKyBkLmdldE1pbnV0ZXMoKVxuXHR0aW1lc3RhbXAuYXBwZW5kVG8gJCgnLm1lc3NhZ2U6bGFzdCcpXG5cbndpbmRvdy51cGRhdGVTY3JvbGxiYXIgPSAtPlxuICBtZXNzYWdlcy5tQ3VzdG9tU2Nyb2xsYmFyKFwidXBkYXRlXCIpLm1DdXN0b21TY3JvbGxiYXIgJ3Njcm9sbFRvJywgJ2JvdHRvbScsIFxuICAgIHNjcm9sbEluZXJ0aWE6IDEwXG4gICAgdGltZW91dDogMFxuXHRcbmZha2VNc2cgPSBbXG5cdFwiSGkgdGhlcmUsIElcXCdtIEtlbGx5IGFuZCB5b3U/XCJcblx0XCJOaWNlIHRvIG1lZXQgeW91XCJcblx0XCJIb3cgYXJlIHlvdSBkb2luZz9cIlxuXHRcIlByZXR0eSBnb29kXCJcblx0XCJIb3dcXCdzIGxpZmUgYmVlbiB0cmVhdGluZyB5b3U/XCJcblx0XCJJdCBjb3VsZCBiZSB3b3JzZSwgdGhhbmtzXCJcblx0XCJJXFwndmUgZ290dGEgZ28gbm93XCJcblx0XCJJdCB3YXMgYSBwbGVhc3VyZSBjaGF0IHdpdGggeW91XCJcblx0XCJCeWUgOilcIlxuXVxuICBcbndpbmRvdy5zZXRGYWtlTWVzc2FnZSA9IC0+XG5cdHR5cGluZyA9ICQoXCI8ZGl2PlwiKS5hcHBlbmQoXCI8c3Bhbj5cIikuYWRkQ2xhc3MgXCJtZXNzYWdlIHR5cGluZ1wiXG5cdHR5cGluZy5hcHBlbmRUbyAkKCcubUNTQl9jb250YWluZXInKVxuXHR1cGRhdGVTY3JvbGxiYXIoKVxuXHRzZXRUaW1lb3V0IC0+XG5cdFx0dHlwaW5nLnJlbW92ZSgpXG5cdFx0bXNnID0gJChcIjxkaXY+XCIpLmFkZENsYXNzIFwibWVzc2FnZVwiXG5cdFx0bXNnLnRleHQgZmFrZU1zZ1tmYWtlTnVtXVxuXHRcdG1zZy5hcHBlbmRUbyAkKCcubUNTQl9jb250YWluZXInKVxuXHRcdHNldERhdGUoKVxuXHRcdHVwZGF0ZVNjcm9sbGJhcigpXG5cdFx0ZmFrZU51bSsrXG5cdCwgMTAwMCArIChNYXRoLnJhbmRvbSgpICogMTApICogMTAwXG5cbndpbmRvdy5pbnNlcnRNZXNzYWdlID0gLT5cblx0bXNnVGV4dCA9ICAkKFwiLmFjdGlvbi1ib3gtaW5wdXRcIikudmFsKClcblx0aWYgJC50cmltKG1zZ1RleHQpID09IFwiXCJcblx0XHRyZXR1cm4gZmFsc2Vcblx0bXNnID0gJChcIjxkaXY+XCIpLmFkZENsYXNzIFwibWVzc2FnZVwiXG5cdG1zZy50ZXh0IG1zZ1RleHRcblx0bXNnLmFkZENsYXNzKFwicGVyc29uYWxcIikuYXBwZW5kVG8gJCgnLm1DU0JfY29udGFpbmVyJylcblx0c2V0RGF0ZSgpXG5cdHVwZGF0ZVNjcm9sbGJhcigpXG5cdCQoXCIuYWN0aW9uLWJveC1pbnB1dFwiKS52YWwobnVsbClcblx0XG5cdCQoXCIubWVzc2FnZS5wZXJzb25hbC50eXBpbmdcIikucmVtb3ZlKClcblx0aXNUeXBpbmcgPSB0cnVlXG5cdGNsZWFyVGltZW91dCB1Y3RUaW1lclxuXHRcblx0aWYgJC50cmltKGZha2VNc2dbZmFrZU51bV0pID09IFwiXCJcblx0XHRyZXR1cm4gZmFsc2Vcblx0c2V0VGltZW91dCAtPlxuXHRcdHNldEZha2VNZXNzYWdlKClcblx0LCA1MDAgKyAoTWF0aC5yYW5kb20oKSAqIDEwKSAqIDEwMFxuXG4kKHdpbmRvdykub24gJ2tleWRvd24nLCAoZSkgLT5cbiAgaWYgKGUud2hpY2ggPT0gMTMpIFxuICAgIGluc2VydE1lc3NhZ2UoKVxuICAgIHJldHVybiBmYWxzZVxuXG4kKHdpbmRvdykubG9hZCAtPlxuXHRtZXNzYWdlcy5tQ3VzdG9tU2Nyb2xsYmFyKClcblx0c2V0VGltZW91dCAtPlxuXHRcdHNldEZha2VNZXNzYWdlKClcblx0LCAxMDBcblx0cmV0dXJuXG5cdFxuJChcIi5hY3Rpb24tYm94LWlucHV0XCIpLm9uIFwia2V5ZG93blwiLCAoZSkgLT5cblx0aWYgJChcIi5hY3Rpb24tYm94LWlucHV0XCIpICE9IFwiXCIgJiYgaXNUeXBpbmcgPT0gdHJ1ZSAmJiBlLndoaWNoICE9IDEzXG5cdFx0dHlwaW5nID0gJChcIjxkaXY+XCIpLmFwcGVuZChcIjxzcGFuPlwiKS5hZGRDbGFzcyBcIm1lc3NhZ2UgcGVyc29uYWwgdHlwaW5nXCJcblx0XHR0eXBpbmcuYXBwZW5kVG8gJCgnLm1DU0JfY29udGFpbmVyJylcblx0XHR1cGRhdGVTY3JvbGxiYXIoKVxuXHRcdGlzVHlwaW5nID0gZmFsc2Vcblx0XHR1c2VyVHlwaW5nQ2xlYXIoKVxuXG4iXX0=
//# sourceURL=coffeescript