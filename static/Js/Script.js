const url = 'https://api.todoist.com/sync/v9/sync'
const token = '778bc7bcc3a75d5837be9ba427447bbe59bbcce4'
headers = new Headers({
    'Authorization': 'Bearer ' + token
});

fetch(url,{
      method :'get',
      headers : headers,

}).then(console.log(data));