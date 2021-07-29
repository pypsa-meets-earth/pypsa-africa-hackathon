# SciGRID gas

What does it provide:

- A routine to create SciGRID_gas data from OSM pbf-files
- A routine to extract meta data from OSM tags
- A segmentation routine for pipelines which will remove some intermediate nodes and create short `PipeSegments`
- An option to remove short pipelines

## Processing.py

def Segments2Lines(Netz):
    Segments=Netz.__dict__['PipeSegments']
    for Segment in Segments:
        if len(Segment.lat)!=len(Segment.node_id):
           startid=Segment.node_id[0]
           endid=Segment.node_id[1]
           new_node_id=[]
           new_node_id.append(startid)
           for i in range(len(Segment.lat)-2):
               new_node_id.append(startid+'-'+str(i+1)+'-'+endid)
           new_node_id.append(endid)
           Segment.node_id=new_node_id
    return Netz

def remove_double_nodes(Netz):
    Segments=Netz.__dict__['PipeSegments']
    for Segment in Segments:
        Segment.lat=Segment.lat[0::2].append(Segment.lat[-1])
        Segment.long=Segment.long[0::2].append(Segment.long[-1])
    return Netz

def rename_nodes(Netz,prestring='LKD_'):
    newnodelist=[]
    complist=Netz.CompLabels()
    for component in complist:
        for element in Netz.__dict__[component]:
            newnodelist=[]
            for node in element.node_id:
                newnodelist.append(prestring+node)
            element.node_id=newnodelist
    complist=Netz.CompLabelsSpot()+['Nodes',]
    for component in complist:
        for element in Netz.__dict__[component]:
            element.id=(prestring+element.id)
    pass


def pipeline_sequencing(lat_list,lon_list,max_length=10):
    '''

    '''
    lat_list2=[]
    lon_list2=[]

    for lat1,lat2,lon1,lon2 in zip(lat_list[:-1],lat_list[1:],lon_list[:-1],lon_list[1:]):
       length=great_circle((lat1,lon1),(lat2,lon2)).km
       if length>max_length:
           lon_avg,lat_avg=midpoint((lon1,lon2),(lat1,lat2))
           lat_tmp1,lon_tmp1=pipeline_sequencing([lat1,lat_avg],[lon1,lon_avg],max_length)
           lat_tmp2,lon_tmp2=pipeline_sequencing([lat_avg,lat2],[lon_avg,lon2],max_length)
           lat_list2.extend(lat_tmp1[:-1])
           lon_list2.extend(lon_tmp1[:-1])
           lat_list2.extend(lat_tmp2)
           lon_list2.extend(lon_tmp2)

       else:
           lat_list2.extend([lat1,lat2])
           lon_list2.extend([lon1,lon2])

       lat_list2=lat_list2[:-1]
       lon_list2=lon_list2[:-1]

    lat_list2.append(lat2)
    lon_list2.append(lon2)
    return lat_list2,lon_list2


def new_node_IDs(Name):
    for i in range(1000000000):
        yield f'{Name}_{i}'


def new_node_ID_nodes():
    for i in range(100000000):
        yield f'SEQ_{i}'

def new_node_ID(x,y):
    for i in range(10000):
        yield x+'-'+y+'_'+str(i)

def old_node_IDs(id_list):
    for i in range(len(id_list)-1):
        yield id_list[i],id_list[i+1]
def average(a,b):
    res_a = (a[0]+a[1])/2
    res_b = (b[0]+b[1])/2
    return res_a,res_b


def paths2nodes(pipelines,IDstring='New',max_distance=10, verbose=True):
    "keep first and last node as the are the only real nodes"
    "create intermediate nodes"
    warning=False
    for pipeline in pipelines:
        if len(pipeline.lat) != len(pipeline.node_id):
            warning=True
    if warning:
        print('Warning: length of id_nodes not equals length of coordinates per pipeline')
    countrydict=CountryPolyDict(TM_World_Borders_file)
    pipenodes=[]
    new_ID_generator=new_node_IDs(IDstring)
    for pipe in pipelines:
        old_nodes = list(zip(pipe.lat,pipe.long))
        lat,long = pipeline_sequencing(pipe.lat,pipe.long,max_length=max_distance)
        new_nodes = list(zip(lat,long))
        #old_ID_generator = old_node_IDs(pipe.node_id)
        new_node_ids = []
        first_id,last_id = pipe.node_id[0],pipe.node_id[-1]
        new_node_ids.append(first_id)
        for i, new_node in enumerate(new_nodes[1:-1]):
            #if new_node in old_nodes:
            #    new_node_ids.append(first_id)
            new_node_ids.append(next(new_ID_generator))


            # if new_nodes[i+1] in old_nodes:
                # if i+1<(len(new_nodes)-1):
                    # first_id,second_id = next(old_ID_generator)
                    # new_ID_generator=new_node_ID(first_id,second_id)
        new_node_ids.append(last_id)
        pipe.node_id=new_node_ids
        pipe.lat=lat
        pipe.long=long
        old_countrycodes=pipe.country_code
        pipe.country_code=GetCountry4List(TM_World_Borders_file,long,lat,countrydict,old_countrycodes)
    if verbose==True:
        print('--Segmenting INET--')

    return pipelines




def create_segments_INET(pipelines,max_distance=10, verbose=True):
    "creates addition pipeline nodes and add them to the network"
    warning=False

