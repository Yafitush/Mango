


def logoutUserByPOST(ip, reqCookie, userName):
    print_frame()
    myHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'X-XSRF-TOKEN': reqCookie['XSRF-TOKEN']}
    try:
        r = requests.post('http://' + ip + ':8080' + '/rest/v1/logout/' + userName, headers=myHeader, cookies=reqCookie)
        if r.status_code == 200 or r.status_code == 201:
            print "Logout!"
        else:
            print "error occurred"
            print "Reason: status code " + str(r.status_code)
            print "Exiting program!"
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print "Error: " + str(e)
        print "Exiting program!"
        sys.exit(1)