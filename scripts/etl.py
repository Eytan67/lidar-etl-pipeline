import pdal

pipeline = """
{
  "pipeline": [
    "/data/100-points-exemple.las",
    {
      "type": "writers.pgpointcloud",
      "connection": "host=pg dbname=lidar user=lidar password=lidar123",
      "table": "points",
      "compression": "dimensional",
      "srid": "4326",
      "overwrite": true
    }
  ]
}
"""

p = pdal.Pipeline(pipeline)
count = p.execute()
print(f" {count} points ingested into PostgreSQL/PostGIS. - again!!!!!!!")