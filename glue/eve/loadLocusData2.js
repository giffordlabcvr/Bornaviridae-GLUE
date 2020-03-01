// Load EVE data from tab file 
var loadResult;
glue.inMode("module/bornaviridaeTabularUtility", function() {
	loadResult = glue.tableToObjects(glue.command(["load-tabular", "tabular/locus/ebv-locus-data.tsv"]));
	//glue.log("INFO", "load result was:", loadResult);
});

_.each(loadResult, function(eveObj) {

	glue.inMode("custom-table-row/locus_data/"+eveObj.sequenceID, function() {
	
		glue.command(["set", "field", "scaffold", eveObj.scaffold]);
		glue.command(["set", "field", "start", eveObj.extract_start]);
		glue.command(["set", "field", "end", eveObj.extract_end]);
		glue.command(["set", "field", "orientation", eveObj.orientation]);
		glue.command(["set", "field", "length", eveObj.sequence_length]);
		glue.command(["set", "field", "assigned_name", eveObj.assigned_name]);
		glue.command(["set", "field", "assigned_gene", eveObj.assigned_gene]);
		glue.command(["set", "field", "bitscore", eveObj.bitscore]);

	});

	glue.inMode("sequence/fasta-eve-digs/"+eveObj.sequenceID, function() {
	
		glue.command(["set", "field", "name", eveObj.sequenceID]);
		glue.command(["set", "field", "full_name", eveObj.sequenceID]);
		glue.command(["set", "field", "genus", eveObj.virus_genus]);
	});

});


