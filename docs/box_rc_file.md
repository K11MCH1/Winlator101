# Box64 `.rcp` Files in Winlator

In Winlator, `.rcp` files are JSON-formatted configuration files that allow
users to define environment variables for specific Windows executables.

These files enable fine-tuning of the Box64 emulator's behavior on a
per-application basis, optimizing performance and compatibility.

---

## What Is an `.rcp` File?

An `.rcp` (Runtime Configuration Profile) file contains structured data that specifies environment variables for individual Windows processes. These variables adjust how Box64 emulates x86_64 applications within Winlator.

The `.rcp` format is unique to Winlator and is not directly compatible with standard Box64 `.box64rc` files. However, `.rcp` files can be used to generate `.box64rc` configurations that Box64 can interpret.

---

## Why Use `.rcp` Files?

RC files are an alternative to adding games as _shortcuts_ in Winlator.
They let you configure settings for specific executables, but in a more
flexible and sharable way. While shortcuts and RC files support different
types of configuration, the big advantage of RC files is that they can be
easily shared and reused.

With community effort, they can grow into large collections of
pre-configured settings for games that need tweaks to run
well in Winlator.

> A good example is the “Luis Gaming” RC file, which comes bundled with
> many forks of Winlator and includes settings for a wide range of games.

## File Structure

An `.rcp` file is a JSON object with the following structure:

- `id`: A unique identifier for the profile.
- `name`: The name of the profile.
- `groups`: An array of groups, each containing:
  - `name`: The group's name.
  - `desc`: A description of the group (optional).
  - `enabled`: A boolean indicating if the group is active.
  - `items`: An array of items, each specifying:
    - `processName`: The name of the executable.
    - `desc`: A description of the item (optional).
    - `vars`: A dictionary of environment variables and their values.

---

## 🛠️ Example `.rcp` Configuration

```json
{
  "name": "Assassin's Creed\/Splinter Cell",
  "desc": "",
  "enabled": true,
  "items": [
    {
      "processName": "AssassinsCreedII.exe",
      "desc": "",
      "vars": {
        "BOX64_DYNAREC_BIGBLOCK": "3",
        "BOX64_DYNAREC_CALLRET": "0",
        "BOX64_DYNAREC_FASTNAN": "1",
        "BOX64_DYNAREC_FASTROUND": "1",
        "BOX64_DYNAREC_SAFEFLAGS": "2",
        "BOX64_MAXCPU": "4"
      }
    },
    {
      "processName": "AssassinsCreedIIGame.exe",
      "desc": "",
      "vars": {
        "BOX64_DYNAREC_BIGBLOCK": "3",
        "BOX64_DYNAREC_CALLRET": "0",
        "BOX64_DYNAREC_FASTNAN": "1",
        "BOX64_DYNAREC_FASTROUND": "1",
        "BOX64_DYNAREC_SAFEFLAGS": "2",
        "BOX64_MAXCPU": "4"
      }
    },
    {
      "processName": "Blacklist_game.exe",
      "desc": "",
      "vars": {
        "BOX64_DYNAREC_BIGBLOCK": "3",
        "BOX64_DYNAREC_CALLRET": "0",
        "BOX64_DYNAREC_FASTNAN": "1",
        "BOX64_DYNAREC_FASTROUND": "1",
        "BOX64_DYNAREC_SAFEFLAGS": "2",
        "BOX64_MAXCPU": "4"
      }
    },
    {
      "processName": "conviction_game.exe",
      "desc": "",
      "vars": {
        "BOX64_DYNAREC_BIGBLOCK": "3",
        "BOX64_DYNAREC_CALLRET": "0",
        "BOX64_DYNAREC_FASTNAN": "1",
        "BOX64_DYNAREC_FASTROUND": "1",
        "BOX64_DYNAREC_SAFEFLAGS": "2",
        "BOX64_MAXCPU": "4"
      }
    }
  ]
}
```

[TODO] Add examples with screen captures of Winlator
