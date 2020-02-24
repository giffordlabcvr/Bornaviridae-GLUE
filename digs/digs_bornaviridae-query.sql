# Get all EVE hits with family and genus
SELECT *
FROM  digs_results, eve_data
WHERE digs_results.assigned_name = eve_data.virus_species
AND   virus_family = "Bornaviridae"
AND bitscore > 60
ORDER BY assigned_name, assigned_gene, bitscore DESC