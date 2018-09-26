# Updating the project schema line
## and working with our new project ODD

As of September 2018, the Digital Mitford has a new TEI ODD to document our project's customization of the TEI Guidelines and to generate our schema validation that guides our encoding. There are two benefits to the ODD:

1. The ODD generates some project-specific documentation of our code, and that means you can look up alphabetically any element we're using in the project and read about what attributes we permit and what values we're using: 
**[Read the ODD Documentation](https://digitalmitford.github.io/DM_documentation/MitfordODD/mitfordODD.html)**
1. The ODD generates new Relax-NG and Schematron validation rules for our project--calling for new schema association lines on our project files.

We would like all active project team members and students to use the new schema and perhaps take some time to compare how it works with the old schema. The new schema should provide more guidance and more clarity on encoding decisions, but we need the team to work with it and give us feedback to improve it. **Here is how to work with the new schema.**

## Instructions 

First, locate the schema lines at the top of your Digital Mitford project file. They appear in purple in oXygen, and are positioned in between the XML declaration line (which looks like this: `<?xml version="1.0" encoding="UTF-8"?>`) and the TEI root element (which looks like this: `<TEI xmlns="http://www.tei-c.org/ns/1.0">`).

Begin by *commenting out* those schema lines. One way to do this is to highlight just the schema lines with your mouse and right-click, and select "Toggle comment" from the drop-down menu in oXygen. Make sure your top lines look like this: 

```
<?xml version="1.0" encoding="UTF-8"?>
<!--<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" 
schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
	schematypens="http://purl.oclc.org/dsdl/schematron"?>
<?xml-model href="http://ebeshero.github.io/MRMValidate.sch" 
type="application/xml" 
schematypens="http://purl.oclc.org/dsdl/schematron"?>-->
<TEI xmlns="http://www.tei-c.org/ns/1.0">

```

(When you do this, you may see an error message that the doument cannot validate without a schema. That's okay--we are about to add a new schema line to associate the new schema.)

Just after the commented-out schema, paste in the following new schema association lines for our ODD-generated schema:

```
<?xml-model href="https://digitalmitford.github.io/DM_documentation/MitfordODD/out/mitfordODD.rng"
type="application/xml" 
schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="https://digitalmitford.github.io/DM_documentation/MitfordODD/out/mitfordODD.rng" 
type="application/xml" 
schematypens="http://purl.oclc.org/dsdl/schematron"?>
```

When complete, the top of your file should look like this, from the XML declaration to the TEI root element:

```
<?xml version="1.0" encoding="UTF-8"?>
<!--<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" 
schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
	schematypens="http://purl.oclc.org/dsdl/schematron"?>
<?xml-model href="http://ebeshero.github.io/MRMValidate.sch" 
type="application/xml" 
schematypens="http://purl.oclc.org/dsdl/schematron"?>-->
<?xml-model href="https://digitalmitford.github.io/DM_documentation/MitfordODD/out/mitfordODD.rng"
type="application/xml" 
schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="https://digitalmitford.github.io/DM_documentation/MitfordODD/out/mitfordODD.rng" 
type="application/xml" 
schematypens="http://purl.oclc.org/dsdl/schematron"?>
```

There's a lot of code at the top of your file for the moment. We'd like you to experiment a little with the schema associations. 
* If you would like to use the old schema, *uncomment* it (remove the XML comment surrounding it), and comment out the *new* schema. 
* When you're ready to work with the new schema again, comment out the old one as we did here, and activate the new one (removing any comment tags around it).

As you work with the new schema, please take note of anything that isn't working as you'd like or that raises questions. If there's anything you'd like us to change about the schema please get in touch with Elisa and Lisa, and we'll make changes. As we update the new schema you won't have to change the schema line--it'll just be updated online here on GitHub and you'll access the changes as you connect to the internet. 