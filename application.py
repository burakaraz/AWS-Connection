from wsgiref.simple_server import make_server
import boto
import uuid
import boto.sdb
import urllib

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)

    conn = boto.sdb.connect_to_region('us-east-1',aws_access_key_id='xxxxxxxxx',aws_secret_access_key='xxxxxxxxx')
    domain = conn.get_domain('Domain-1')

    response = "Hello, Welcome! "

    response = "Response to the query "
    query = environ['QUERY_STRING']
    query_string = query.split("=", 1)
    if len(query_string) > 1:
    	final_query = urllib.unquote(query_string[1])
    else:
        response = "Please enter query! "
        return [response]

    query = 'select * from `Domain-1` ' + final_query + ' and ID IS NOT NULL ORDER BY ID ASC'
    result_query = domain.select(query)
    #print final_query
    response = response + final_query
    #print response
    response = response + "\n"
    for obj in result_query:
    	#response = response + \
    	if obj["ID"] != "" :
    		obj_id = obj["ID"]
    		response = response + "\n"
    		response = response + "Id: "
    		response = response + str(obj_id)
    	if obj["Category"] != "":
    		obj_category = obj["Category"]
    		response = response + "\n\t"  
    		response = response + "Category: "
    		response = response + str(obj_category)
    	if obj["Title"] != "":
    		obj_title = obj["Title"]  
    		response = response + "\n\t"
    		response = response + "Title: "
    		response = response + str(obj_title)
    	if obj["BasedOn"] != "":
    		obj_base = obj["BasedOn"]  
    		response = response + "\n\t"
    		response = response + "BasedOn: "
    		response = response + str(obj_base)
    	if obj["Year"] != "":
    		obj_year = obj["Year"]  
    		response = response + "\n\t"
    		response = response + "Year: "
    		response = response + str(obj_year)
    	if obj["StartYear"] != "":
    		obj_startyear = obj["StartYear"]  
    		response = response + "\n\t"
    		response = response + "StartYear: "
    		response = response + str(obj_startyear)
    	if obj["EndYear"] != "":
    		obj_endyear = obj["EndYear"]  
    		response = response + "\n\t"
    		response = response + "EndYear: "
    		response = response + str(obj_endyear)
    	if obj["NumberOfEpisodes"] != "":
    		obj_noe = obj["NumberOfEpisodes"]  
    		response = response + "\n\t"
    		response = response + "NumberOfEpisodes: "
    		response = response + str(obj_noe)
    	if obj["Duration"] != "":
    		obj_dur = obj["Duration"]  
    		response = response + "\n\t"
    		response = response + "Duration: "
    		response = response + str(obj_dur)
    	if obj["Director"] != "":
    		obj_dir = obj["Director"]  
    		response = response + "\n\t"
    		response = response + "Director: "
    		response = response + str(obj_dir)
    	if obj["Producer"] != "\r\n":
    		obj_prod = obj["Producer"]  
    		response = response + "\n\t"
    		response = response + "Producer: "
    		response = response + str(obj_prod)
    	#print obj["Producer"]
    return [response]


if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print "Serving on port 8000..."
    httpd.serve_forever()
