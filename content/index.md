---
publish: true
title: FMeinicke's Wiki
created: 2025-07-04T08:16:31.946+02:00
modified: 2026-02-09T14:24:39.000+01:00
published: 2026-02-09T14:24:39.000+01:00
---

```dataviewjs
const folders = dv.pages('"Wiki"').where(p => p.file.name != "Wiki").groupBy(page => page.file.folder);
const folder_lists = folders.map(folder => {
    const folder_path = folder.key.replace("Wiki", "");
    const indent = folder_path.split("/").length - 1;
    const folder_name = folder_path.split("/").last();
    const folder_link = folder.key; //.replaceAll(" ", "-").replaceAll("&", "-and-");
    const folder_el = indent > 0 ? `${"  ".repeat(indent)}- ${dv.page(folder_name) ? dv.fileLink(folder_link, false, folder_name) : folder_name}` : "";
    const folders_without_folder_notes = folder.rows.where(r => folder_name != r.file.name);
    const pages_list = folders_without_folder_notes.file.link.map(row => `${"  ".repeat(indent + 1)}- ${row}`).sort().join("\n");
    return `${folder_el}`;
});
dv.paragraph(dv.markdownList(folder_lists.join("\n")));
```
