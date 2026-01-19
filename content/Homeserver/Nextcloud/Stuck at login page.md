---
publish: true
created: 2025-07-28T09:37:19.862+02:00
modified: 2025-07-29T17:33:46.000+02:00
published: 2025-07-29T17:33:46.000+02:00
cssclasses: ""
---


#nextcloud #nginx-proxy-manager

> [!info] Source
> 
> - <https://www.reddit.com/r/NextCloud/comments/tnyv51/nextcloud_infinite_login_loop/>
> - <https://help.nextcloud.com/t/session-error-token-expired-on-browser-login/224487>
> - <https://github.com/nextcloud/all-in-one/blob/750cd365cc3c0457bc9e6c2bd309b59bda5d652a/reverse-proxy.md#nginx-proxy-manager---npm>

- clear the browser cache and delete all cookies, then refresh the login page (make sure the URL ends with `/login` and doesn't have any query parameters at the end)
- ensure that the NPM proxy configuration has the *Cache Assets* option **disabled**
