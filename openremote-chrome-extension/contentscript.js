function onText(data) {
    // Create the overlay at the top of the page and fill it with data.
    var status_dom = document.getElementById("openremote_status_div");
    if(status_dom) {
      document.body.removeChild(status_dom);      
    }
    
    status_dom = document.createElement('div');
    status_dom.id = "openremote_status_div"
    status_dom.style.background = '#237';
    status_dom.style.opacity = '0.85';
    status_dom.style.color = '#fff';
    status_dom.style.padding = '10px';
    status_dom.style.position = 'fixed';
    status_dom.style.top = '0px';
    status_dom.style.left = '0px';
    status_dom.style.width = '100%';
    status_dom.style.zIndex = '123456';
    status_dom.style.font = '14px sans-serif';
    status_dom.style.textAlign = 'left';

    var title_dom = document.createElement('strong');
    title_dom.innerText = 'URLRemote: ';
    status_dom.appendChild(title_dom);

    var text_dom = document.createTextNode(data);
    status_dom.appendChild(text_dom);

    var close_link = document.createElement('a');
    close_link.innerText = "Close"
    close_link.onclick = function() {document.body.removeChild(status_dom); };
    close_link.style.cursor = 'pointer';
    close_link.style.textDecoration = 'underline';
    close_link.style.textAlign = 'right';
    close_link.style.position = 'absolute';
    close_link.style.right = '30px';    
    close_link.style.color = "#fff";
    close_link.style.background = '#237';
    close_link.style.font = '14px sans-serif';
    status_dom.appendChild(close_link);

    document.body.insertBefore(status_dom, document.body.firstChild);  
};

// Send a request to fetch response data from the background page.
// Specify that onText should be called with the result.
chrome.extension.sendRequest({'action' : 'getRemoteBrowserResponse'}, onText);
