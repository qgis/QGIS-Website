#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Optimize changelog images in visual-changelogs.

This script performs the following tasks:
1. Optimizes images for web usage by rescaling them
2. Converts non-gif images to webp format
3. Updates index.md to use the new webp images
"""

import os
import re
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is not installed.")
    print("Install it with: pip install Pillow")
    sys.exit(1)


class ChangelogOptimizer:
    def __init__(self, changelog_dir):
        self.changelog_dir = Path(changelog_dir)
        self.images_dir = self.changelog_dir / "images"
        self.entries_dir = self.images_dir / "entries"
        self.index_md = self.changelog_dir / "index.md"
        
        # Image configuration
        self.max_width = 1200
        self.max_height = 800
        self.quality = 85
        
    def get_referenced_images(self):
        """Extract all image references from index.md"""
        referenced = set()
        
        if not self.index_md.exists():
            print(f"Warning: {self.index_md} not found")
            return referenced
        
        with open(self.index_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references: ![...](images/entries/...)
        pattern = r'!\[.*?\]\(images/entries/([^)]+)\)'
        matches = re.findall(pattern, content)
        
        for match in matches:
            # match is now just the filename
            referenced.add(match)
        
        return referenced
    
    def optimize_image(self, image_path):
        """
        Optimize a single image:
        - Rescale for web
        - Convert to webp (except gif)
        - Rescale gif but keep as gif
        Returns the new filename if converted, None if skipped or kept as is
        """
        try:
            # Open and process the image
            img = Image.open(image_path)
            
            # Get original size
            orig_width, orig_height = img.size
            
            # Calculate scaling to fit within max dimensions
            scale = min(self.max_width / orig_width, self.max_height / orig_height, 1.0)
            
            # Check if rescaling is needed
            needs_rescale = scale < 1.0
            is_gif = image_path.suffix.lower() == '.gif'
            
            if not needs_rescale and not is_gif:
                print(f"  Skipping: {image_path.name} (no optimization needed)")
                return None
            
            if needs_rescale:
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                size_info = f"{orig_width}x{orig_height} → {new_width}x{new_height}"
            else:
                size_info = f"{orig_width}x{orig_height} (no resize needed)"
            
            # Handle GIF separately (keep as gif)
            if is_gif:
                if needs_rescale:
                    img.save(image_path, 'GIF', optimize=True)
                    print(f"  Optimized GIF: {image_path.name} ({size_info})")
                    return None
                else:
                    print(f"  Skipping GIF: {image_path.name}")
                    return None
            
            # Convert RGBA to RGB for webp (if needed)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as webp. For a file whose name already ends in .webp
            # (including the harvester's name.png.webp convention) the target
            # name equals the source name, so the image is optimized in place
            # and there is nothing to delete. Deleting unconditionally used to
            # destroy exactly those files: the optimized copy was written over
            # the original and then unlinked, while index.md kept referencing
            # it.
            new_filename = image_path.stem + '.webp'
            new_path = image_path.parent / new_filename

            # Write atomically so a failed save cannot leave a truncated or
            # missing image behind.
            tmp_path = new_path.with_name(new_path.name + '.tmp')
            img.save(tmp_path, 'WEBP', quality=self.quality, method=6)
            os.replace(tmp_path, new_path)

            if new_path == image_path:
                print(f"  Optimized in place: {image_path.name} ({size_info})")
                return None

            # Delete the original only now that the replacement exists.
            image_path.unlink()

            print(f"  Optimized: {image_path.name} → {new_filename} ({size_info})")
            return new_filename

        except Exception as e:
            print(f"  Error processing {image_path.name}: {e}")
            # Remove a partially written temporary file if the save failed.
            tmp_path = image_path.parent / (image_path.stem + '.webp.tmp')
            if tmp_path.exists():
                tmp_path.unlink()
            return None
    
    def optimize_images(self):
        """Optimize all referenced images"""
        if not self.entries_dir.exists():
            print("Warning: Images directory not found")
            return {}
        
        referenced = self.get_referenced_images()
        conversions = {}  # old_name -> new_name mapping
        
        print(f"Optimizing {len(referenced)} referenced images:")
        
        for filename in sorted(referenced):
            file_path = self.entries_dir / filename
            
            if not file_path.exists():
                print(f"  Warning: Referenced image not found: {filename}")
                continue
            
            new_filename = self.optimize_image(file_path)
            if new_filename:
                conversions[filename] = new_filename
        
        return conversions
    
    def update_index_md(self, conversions):
        """Update index.md to use new webp images"""
        if not conversions:
            print("✓ No image references to update")
            return
        
        with open(self.index_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Updating {len(conversions)} image references in index.md:")
        
        for old_name, new_name in sorted(conversions.items()):
            old_ref = f"images/entries/{old_name}"
            new_ref = f"images/entries/{new_name}"
            
            if old_ref in content:
                content = content.replace(old_ref, new_ref)
                print(f"  Updated: {old_name} → {new_name}")
        
        with open(self.index_md, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated index.md")
    
    def verify_references(self):
        """Check that every image referenced by index.md exists on disk.

        Returns the sorted list of missing filenames. A silent mismatch here
        is how gallery images can disappear while index.md keeps pointing at
        them, so callers should treat a non-empty result as a failure.
        """
        missing = sorted(
            name for name in self.get_referenced_images()
            if not (self.entries_dir / name).exists()
        )
        for name in missing:
            print(f"  Missing referenced image: images/entries/{name}")
        return missing

    def process(self):
        """Run all optimization tasks; return the number of broken references"""
        print(f"\n{'='*60}")
        print(f"Processing: {self.changelog_dir.name}")
        print(f"{'='*60}\n")

        # Step 1: Optimize images
        print("Step 1: Optimizing images")
        conversions = self.optimize_images()

        # Step 2: Update index.md
        print("\nStep 2: Updating index.md")
        self.update_index_md(conversions)

        # Step 3: Fail loud when a referenced image is missing, instead of
        # leaving broken references behind silently.
        print("\nStep 3: Verifying image references")
        missing = self.verify_references()
        if missing:
            print(f"✗ {self.changelog_dir.name}: {len(missing)} referenced image(s) missing")
        else:
            print("✓ All referenced images exist")

        print(f"\n✓ Completed processing: {self.changelog_dir.name}\n")
        return len(missing)


def main():
    """Process all visual changelogs or a specific one"""
    changelogs_base = Path("content/project/visual-changelogs")
    
    if not changelogs_base.exists():
        print(f"Error: {changelogs_base} not found")
        return
    
    # Check if a specific changelog was provided
    if len(sys.argv) > 1:
        changelog_name = sys.argv[1]
        changelog_dir = changelogs_base / changelog_name
        
        if not changelog_dir.exists():
            print(f"Error: {changelog_dir} not found")
            return
        
        optimizer = ChangelogOptimizer(changelog_dir)
        missing = optimizer.process()
        if missing:
            sys.exit(f"{changelog_name}: {missing} referenced image(s) missing")
    else:
        # Process all changelogs
        changelog_dirs = sorted([d for d in changelogs_base.iterdir() if d.is_dir()])

        print(f"\nFound {len(changelog_dirs)} changelogs to process\n")

        total_missing = 0
        for changelog_dir in changelog_dirs:
            optimizer = ChangelogOptimizer(changelog_dir)
            total_missing += optimizer.process()

        print(f"\n{'='*60}")
        if total_missing:
            print(f"✗ Done, but {total_missing} referenced image(s) are missing (see above)")
            print(f"{'='*60}\n")
            sys.exit(1)
        print("✓ All changelogs processed successfully!")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
