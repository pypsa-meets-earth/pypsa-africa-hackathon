# SciGRID power

<!-- 
    def create_tables(self):
    # Create tables necessary for the abstraction process. 
        create_tables(self.cur, self.conn)
        i.e def ct__vertices(cur,conn):
          # Create _vertices table."""
          
          DROP TABLE IF EXISTS _vertices;
          CREATE TABLE _vertices (
          id              serial PRIMARY KEY NOT NULL, 
          osm_id          bigint,
          osm_id_typ      char, 
          geo_center      geometry,
          longitude       float,
          latitude        float,
          role            text,
          voltage         text,
          from_relation   bigint);
          """
    
    def analyze_relations(self):
    # Analyze the power relations. 
        msg = analyze_rels(self.cur, self.conn)
        return msg
    
        """ The relations analysis analyzes how many relations exists in the OSM database 
        whith a voltage tag having a value of 220kV and higher. 
        It also defines how many relations are incomplete or are in planning/under construction.
        Further, information about the number of substations and line segements is collected.
 
        This relations analysis is structured as follows:
        Three functions are defined which use the filteres power relation IDs as an input value. 
        The first function "get_rel_parts_with_power_vals" return the elements of the relation having a voltage tag, 
        and the second function "get_rel_parts_without_power_vals" returns the elements of the relation without a voltage tag. 
        The third function "analysis_rel" analyzes the relations and stores the results into the table _analysis_rels.
        The table will be used in the abstraction step.
        """
    
    def abstract_relations(self):
	# Execute the abstraction. 
        msg = ra.abstract_2subs(self.cur, self.conn)
        success = ra.abstract_3subs_T_node(self.cur, self.conn)
        #TODO: ra.abstract_3subs_in_row(self.cur, self.conn)
        return len(msg) + success
        
        """
        Abstracting relations which have exactly 2 stations to vertices and links.
        Vertices: Substations are in general polygons (which applies to the tags "substation", "generator", "station", "switch", 
        etc. The substations are abstracted as a vertex, which is the geometric center of their constituing polygon. 
        If a substation is a node in OpenStreetmap, then the vertex is this node.
        If a station is of type "relation" in OpenStreetMap, the rectangle which includes all nodes of the relation is 
        defined and its center is used as a vertex. 
        To define which relations in OpenStreetMap have exacly two substations, relations analysis is performed in
        relation_analysis.py and the results are to be found in the table _analysis_rels.
        
        Links: Relation are made of one or more links (transmission lines). These transmission lines are abstracted as the
        links between the two vertices obtained when abstracting the substations. The actual length of the transmission lines
        is calculated as sum of the line (and cables) segments length, which are also listed as constituing the relation.    
        """ 
        
        
    def add_electrical_properties(self):
	# Calculate the electrical properties of the transmission lines using the dena assumptions. 
        nr_success = ep.add_dena_assumptions(self.cur, self.conn)
        return nr_success -->
