#!/usr/bin/env python
# coding: utf-8

# In[49]:


from lxml import etree
import xml.etree.ElementTree as ET


tree = ET.parse('FormTemplate.xml')
root = tree.getroot()
page = etree.Element("Layout")
doc = etree.ElementTree(page)

para1 = """<ParaStyle>
    <Id>86</Id>
    <Name>Normal 6</Name>
    <Comment/>
    <ParentId>Def.ParaStyleGroup</ParentId>
    <IndexInParent>8</IndexInParent>
    <SecurityDescriptorId>-1</SecurityDescriptorId>
    <Forward/>
  </ParaStyle>"""

para2 = """<ParaStyle>
    <Id>86</Id>
    <AncestorId/>
    <LeftIndent>0</LeftIndent>
    <RightIndent>0</RightIndent>
    <FirstLineLeftIndent>0</FirstLineLeftIndent>
    <SpaceBefore>0</SpaceBefore>
    <SpaceAfter>0</SpaceAfter>
    <LineSpacing>6.7232387112511505e-002</LineSpacing>
    <LineSpacingType>Exact</LineSpacingType>
    <DefaultTextStyleId>Def.TextStyleDelta</DefaultTextStyleId>
    <NextParagraphStyleId/>
    <BorderStyleId/>
    <NewAreaPageAfter>None</NewAreaPageAfter>
    <HAlign>Left</HAlign>
    <IsVisible>True</IsVisible>
    <ConnectBorders>False</ConnectBorders>
    <WithLineGap>False</WithLineGap>
    <BullettingId/>
    <IgnoreEmptyLines>False</IgnoreEmptyLines>
    <TabulatorProperties>
      <Default>1.2500000000000001e-002</Default>
      <UseOutsideTabs>False</UseOutsideTabs>
    </TabulatorProperties>
    <Hyphenation>
      <Hyphenate>False</Hyphenate>
      <MinLeft>2</MinLeft>
      <MinRight>2</MinRight>
      <MaxConsecutive>2</MaxConsecutive>
    </Hyphenation>
    <Orphan>1</Orphan>
    <Widow>1</Widow>
    <NumberingType>None</NumberingType>
    <NumberingVariableId/>
    <NumberingFrom>1</NumberingFrom>
    <SpaceBeforeFirst>False</SpaceBeforeFirst>
    <KeepLinesTogether>No</KeepLinesTogether>
    <KeepWithNext>False</KeepWithNext>
    <KeepWithPrevious>False</KeepWithPrevious>
    <DontWrap>False</DontWrap>
    <RightReadingOrder>False</RightReadingOrder>
    <Reversed>False</Reversed>
    <CutFreely>False</CutFreely>
    <CalcMaxSpaceBeforeAfter>False</CalcMaxSpaceBeforeAfter>
    <NewAreaPageBefore>None</NewAreaPageBefore>
    <DistributeLineSpace>False</DistributeLineSpace>
    <Type>Simple</Type>
    <Css>
      <File/>
      <ClassSelectorType>None</ClassSelectorType>
    </Css>
  </ParaStyle>"""

para3 = """<TextStyle>
    <Id>87</Id>
    <Name>Normal 9</Name>
    <Comment/>
    <ParentId>Def.TextStyleGroup</ParentId>
    <IndexInParent>12</IndexInParent>
    <SecurityDescriptorId>-1</SecurityDescriptorId>
    <Forward/>
  </TextStyle>"""

para4= """<TextStyle>
    <Id>87</Id>
    <AncestorId/>
    <FontSize>3.8946642981635199e-003</FontSize>
    <LineWidth>0</LineWidth>
    <MiterLimit>10</MiterLimit>
    <BaselineShift>0</BaselineShift>
    <InterCharacterSpacing>0</InterCharacterSpacing>
    <OutlineStyleId/>
    <FillStyleId>83</FillStyleId>
    <CapType>Butt</CapType>
    <JoinType>Miter</JoinType>
    <Kerning>False</Kerning>
    <BorderStyleId/>
    <IsVisible>True</IsVisible>
    <ConnectBorders>False</ConnectBorders>
    <WithLineGap>False</WithLineGap>
    <FontId>80</FontId>
    <SubFont>Regular</SubFont>
    <Bold>False</Bold>
    <Italic>False</Italic>
    <Underline>False</Underline>
    <Strikethrough>False</Strikethrough>
    <Language>en</Language>
    <SmallCap>False</SmallCap>
    <SuperScript>False</SuperScript>
    <SubScript>False</SubScript>
    <SuperScriptOffset>0.33000000000000002</SuperScriptOffset>
    <SubScriptOffset>0.33000000000000002</SubScriptOffset>
    <SuperSubScriptSize>0.57999999999999996</SuperSubScriptSize>
    <AffectSuperSubScriptUnderline>True</AffectSuperSubScriptUnderline>
    <AffectSuperSubScriptStrikethrough>True</AffectSuperSubScriptStrikethrough>
    <SmallCapSize>0.69999999999999996</SmallCapSize>
    <CustomUnderlineStrikethrough>False</CustomUnderlineStrikethrough>
    <UnderlineOffset>0.106</UnderlineOffset>
    <UnderlineWidth>7.2999999999999995e-002</UnderlineWidth>
    <StrikethroughOffset>0.23599999999999999</StrikethroughOffset>
    <StrikethroughWidth>7.2999999999999995e-002</StrikethroughWidth>
    <URLLink/>
    <HorizontalScale>100</HorizontalScale>
    <WrappingRuleId/>
    <Type>Simple</Type>
    <UnderlineLineStyleId/>
    <StrikethroughLineStyleId/>
    <ShadowStyleId/>
    <ShadowStyleOffset X="0" Y="0"/>
    <IsFixedWidth>False</IsFixedWidth>
    <FixedWidth>3.0000000000000001e-003</FixedWidth>
    <Css>
      <File/>
      <ClassSelectorType>None</ClassSelectorType>
    </Css>
  </TextStyle>"""

for elem in root:
    pageElement = etree.SubElement(page, elem.tag)
    for subelem in elem:
        if len(subelem.attrib)!= 0:
            s = etree.SubElement(pageElement, subelem.tag, attrib=subelem.attrib)
        else:
            s = etree.SubElement(pageElement, subelem.tag)
        s.text = subelem.text
                
        for subsubelem in subelem:
            if len(subsubelem.attrib)!= 0:
                 k = etree.SubElement(s, subsubelem.tag, attrib=subsubelem.attrib)
            else:
                 k = etree.SubElement(s, subsubelem.tag)
            k.text = subsubelem.text
            for subsubsubelem in subsubelem:
                if len(subsubsubelem.attrib)!= 0:
                    l = etree.SubElement(k, subsubsubelem.tag,  attrib=subsubsubelem.attrib)
                else:
                    l = etree.SubElement(k, subsubsubelem.tag)
                l.text = subsubsubelem.text

root_1 = ET.fromstring(para1)

pageElement = etree.SubElement(page, root_1.tag)
for child in root_1:
    s = etree.SubElement(pageElement, child.tag)
    s.text = child.text

root_2 = ET.fromstring(para2)
pageElement = etree.SubElement(page, root_2.tag)
for child in root_2:
    s = etree.SubElement(pageElement, child.tag)
    s.text = child.text
    for subchild in child:
        if len(subchild.attrib)!= 0:
            k = etree.SubElement(s, subchild.tag, attrib=subchild.attrib)
        else:
            k = etree.SubElement(s, subchild.tag)
        k.text = subchild.text
        for subsubchild in subchild:
            if len(subsubchild.attrib)!= 0:
                l = etree.SubElement(k, subsubchild.tag, attrib=subsubchild.attrib)
            else:
                l = etree.SubElement(k, subsubchild.tag)
            l.text = subsubchild.text

root_3 = ET.fromstring(para3)
pageElement = etree.SubElement(page, root_3.tag)
for child in root_3:
    s = etree.SubElement(pageElement, child.tag)
    s.text = child.text
    for subchild in child:
        if len(subchild.attrib)!= 0:
            k = etree.SubElement(s, subchild.tag, attrib=subchild.attrib)
        else:
            k = etree.SubElement(s, subchild.tag)
        k.text = subchild.text
        for subsubchild in subchild:
            if len(subsubchild.attrib)!= 0:
                l = etree.SubElement(k, subsubchild.tag, attrib=subsubchild.attrib)
            else:
                l = etree.SubElement(k, subsubchild.tag)
            l.text = subsubchild.text

            
            
root_4 = ET.fromstring(para4)
pageElement = etree.SubElement(page, root_4.tag)
for child in root_4:
    s = etree.SubElement(pageElement, child.tag)
    s.text = child.text
    for subchild in child:
        if len(subchild.attrib)!= 0:
            k = etree.SubElement(s, subchild.tag, attrib=subchild.attrib)
        else:
            k = etree.SubElement(s, subchild.tag)
        k.text = subchild.text
        for subsubchild in subchild:
            if len(subsubchild.attrib)!= 0:
                l = etree.SubElement(k, subsubchild.tag, attrib=subsubchild.attrib)
            else:
                l = etree.SubElement(k, subsubchild.tag)
            l.text = subsubchild.text
            
doc.write('FormTemplate_Test2.xml', xml_declaration=True, encoding='utf-8')

print('XML generated')


# In[ ]:




